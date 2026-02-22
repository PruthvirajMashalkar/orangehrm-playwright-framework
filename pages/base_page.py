from utils.logger import get_logger

class BasePage:
    
    def __init__(self, page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def click(self, locator):
        self.logger.info(f"Clicking on {locator}")
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.logger.info(f"Filling {locator} with {value}")
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        text = self.page.locator(locator).text_content()
        self.logger.info(f"Text from {locator}: {text}")
        return text