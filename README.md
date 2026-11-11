# Автоматизированное тестирование SauceDemo

UI-тесты для https://www.saucedemo.com/ на Python, pytest и Playwright.

| Тест | Проверка |
|---|---|
| `test_login_page_is_displayed` | Поля логина, пароля и кнопка входа видимы |
| `test_successful_login` | Успешная авторизация и открытие каталога |
| `test_add_product_to_cart` | Добавление рюкзака и индикатор корзины `1` |
| `test_login_with_invalid_password` | Ошибка при неправильном пароле |

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```
