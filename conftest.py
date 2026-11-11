"""Record actual page state for the lab report without changing test scenarios."""
import json
import os
from pathlib import Path

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call":
        return
    evidence = {
        "nodeid": item.nodeid,
        "outcome": report.outcome,
        "duration_seconds": report.duration,
    }
    page = item.funcargs.get("page")
    if page is not None and not page.is_closed():
        evidence["url"] = page.url
        try:
            evidence["dom"] = page.evaluate("""() => ({
                title: document.title,
                username_visible: !!document.querySelector('[data-test="username"]')?.getClientRects().length,
                password_visible: !!document.querySelector('[data-test="password"]')?.getClientRects().length,
                login_button_visible: !!document.querySelector('[data-test="login-button"]')?.getClientRects().length,
                inventory_visible: !!document.querySelector('[data-test="inventory-container"]')?.getClientRects().length,
                cart_badge: document.querySelector('[data-test="shopping-cart-badge"]')?.textContent ?? null,
                error: document.querySelector('[data-test="error"]')?.textContent ?? null,
                backpack_button: document.querySelector('[data-test="remove-sauce-labs-backpack"]')?.textContent ?? null
            })""")
        except Exception as error:
            evidence["capture_error"] = str(error)
    run = os.environ.get("LAB5_RUN_ID")
    if run:
        folder = Path(__file__).resolve().parent.parent / "report/logs" / f"{run}_evidence"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / f"{item.name}.json").write_text(
            json.dumps(evidence, ensure_ascii=False, indent=2) + "\n"
        )
