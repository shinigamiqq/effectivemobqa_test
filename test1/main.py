import pytest
from playwright.sync_api import sync_playwright
import time


@pytest.mark.parametrize(
    "USERNAME, PASSWORD",
    [
        ("standard_user", "secret_sauce")
    ]
)
def test_saucedemo_purchase(USERNAME, PASSWORD):
    """Функция, тестирующая функционал магазина"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        time.sleep(2)

        page.fill("input[name='user-name']", USERNAME)
        page.fill("input[name='password']", PASSWORD)
        time.sleep(2)

        page.click("input[type='submit']")
        assert page.is_visible("text=Products")

        page.click("text='Sauce Labs Backpack'")
        time.sleep(2)

        page.click("button:has-text('Add to cart')")
        time.sleep(2)

        page.click("a.shopping_cart_link")

        assert page.is_visible("text='Sauce Labs Backpack'")

        page.click("button:has-text('Checkout')")
        time.sleep(2)

        page.fill("input[name='firstName']", "Bill")
        time.sleep(2)
        page.fill("input[name='lastName']", "Mamo")
        time.sleep(2)
        page.fill("input[name='postalCode']", "144852")
        time.sleep(2)
        page.click("input[type='submit']")
        time.sleep(2)
        page.click("button:has-text('Finish')")
        time.sleep(2)

        assert page.is_visible("text='Thank you for your order!'")
        time.sleep(2)

        browser.close()


