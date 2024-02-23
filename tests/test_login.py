from playwright.sync_api import Page
from utils.config import Config

class TestLogin:
    config = Config()

    def test_login(self, page: Page):
        page.goto("https://www.saucedemo.com/")
        page.fill("id=user-name", "standard_user")
        page.fill("id=password", "secret_sauce")
        page.click("id=login-button")

        assert page.is_visible(".title")
        assert page.is_visible("id=inventory_container")
