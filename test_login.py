from playwright.sync_api import Page, expect


def test_login_page_is_displayed(page: Page):
    page.goto("https://www.saucedemo.com/")

    expect(page.locator('[data-test="username"]')).to_be_visible()
    expect(page.locator('[data-test="password"]')).to_be_visible()
    expect(page.locator('[data-test="login-button"]')).to_be_visible()


def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(
        page.locator('[data-test="inventory-container"]')
    ).to_be_visible()


def test_add_product_to_cart(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    expect(
        page.locator('[data-test="inventory-container"]')
    ).to_be_visible()

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    expect(
        page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_text("1")


def test_login_with_invalid_password(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("wrong_password")
    page.locator('[data-test="login-button"]').click()

    expect(
        page.locator('[data-test="error"]')
    ).to_be_visible()

    expect(
        page.locator('[data-test="error"]')
    ).to_contain_text("Username and password do not match")
