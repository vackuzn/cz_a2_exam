from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class SelWrapper:
    def load_url(self, url: str):
        self._driver.get(url)
        # sleep(2)
        elems = self._driver.find_elements(By.CSS_SELECTOR, "#select-town .btn")

        a = 5

    def __enter__(self):
        self._driver = webdriver.Firefox()
        return self

    def __exit__(self, *args):
        self._driver.close()
