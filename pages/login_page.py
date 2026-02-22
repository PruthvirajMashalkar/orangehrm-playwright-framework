from pages.base_page import BasePage
from config.config import BASE_URL

class LoginPage(BasePage):
    
    def navigate(self):
        self.page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)

    def login_with_enter(self, username, password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_placeholder("Password").press("Enter")
    
    def login(self, username, password):
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def get_error_message(self):
        return self.page.get_by_role("alert").text_content()

    def get_required_messages(self):
        return self.page.locator(".oxd-input-field-error-message").all_text_contents()

    def is_password_masked(self):
        return self.page.get_by_placeholder("Password").get_attribute("type") == "password"