from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from Config.config import TestData


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(by_locator).click()

    def page_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        ttl = self.driver.title
        print("\n Current Page Title:", ttl)
        assert self.driver.title == title
