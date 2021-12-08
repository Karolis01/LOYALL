from Config.config import TestData
from Pages.PageActions import PageActions
from Tests.test_base import BaseTest


class TestOurSolutions(BaseTest):

    def test_loyalty_program_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.click(TestData.LOYALTY_PROGRAM)
        self.pageActions.check_title(TestData.LOYALTY_PROGRAM_TITLE)

    def test_loyalty_partner_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.click(TestData.LOYALTY_PARTNER)
        self.pageActions.check_title(TestData.LOYALTY_PARTNER_TITLE)

    def test_costumer_registration_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.click(TestData.COSTUMER_REGISTRATION)
        self.pageActions.check_title(TestData.COSTUMER_REGISTRATION_TITLE)

    def test_data_collection_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.click(TestData.DATA_COLLECTION)
        self.pageActions.check_title(TestData.DATA_COLLECTION_TITLE)

    def test_marketing_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.click(TestData.MARKETING)
        self.pageActions.check_title(TestData.MARKETING_TITLE)

    def test_gift_cards_page(self):
        self.pageActions = PageActions(self.driver)
        self.pageActions.click(TestData.GIFT_CARDS)
        self.pageActions.check_title(TestData.GIFT_CARDS_TITLE)
