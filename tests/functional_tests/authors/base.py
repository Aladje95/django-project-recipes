import time
from selenium.webdriver.common.by import By


from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser


class AuthorsBaseTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, qtd=10):
        time.sleep(qtd)

    def get_by_placeholder(self, element, placeholder_text):
        return element.find_element(By.XPATH, f'.//input[@placeholder="{placeholder_text}"]')
