from Config.config import TestData
from Pages.BasePage import BasePage


class PageActions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def check_title(self, title):
        self.page_title(title)

    def click(self, by_locator):
        self.do_click(by_locator)
