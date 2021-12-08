from selenium.webdriver.common.by import By


class TestData:
    BASE_URL = "https://www.loyall.io/"

    LOYALTY_PROGRAM = "//div[@class='color-block']//img[@alt='Handshake that illustrates loyalty.']"
    LOYALTY_PARTNER = "//div[@class='color-block']//img[@alt='Icon of Loyalty Partner Program']"
    COSTUMER_REGISTRATION = "//div[@class='color-block']//img[@alt='Two circles that link together']"
    DATA_COLLECTION = "//div[@class='color-block']//img[@alt='Icons such as wifi, cloud, internet that represents data collection.']"
    MARKETING = "//div[@class='color-block']//img[contains(@alt,'Megaphone that symbolize marketing.')]"
    GIFT_CARDS = "//div[@class='color-block']//img[@alt='A gift card']"

    LOYALTY_PROGRAM_TITLE = "Loyalty Program that increases revenue and loyalty | Loyall"
    LOYALTY_PARTNER_TITLE = "Loyalty Partner Program automates discounts & bonuses | Loyall"
    COSTUMER_REGISTRATION_TITLE = "Hvordan fungerer digital smitteregistrering?"
    DATA_COLLECTION_TITLE = "Automatic data collection via WiFi | Loyall"
    MARKETING_TITLE = "We make your marketing more successful | Loyall"
    GIFT_CARDS_TITLE = "Increase sales with custom gift cards | Loyall"


