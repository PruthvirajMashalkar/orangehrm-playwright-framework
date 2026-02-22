from pages.base_page import BasePage
from config.config import BASE_URL

class AdminPage(BasePage):
    def navigate_to_admin(self):
        self.page.get_by_role("link", name="Admin").click()

    def click_add(self):
        self.page.get_by_role("button", name="Add").click()

    def select_user_role(self, role_name="Admin"):
        dropdown = (
        self.page
        .locator("label:has-text('User Role')")
        .locator("xpath=following::div[contains(@class,'oxd-select-text')][1]")
        )

        dropdown.click()

        # Wait for dropdown listbox
        listbox = self.page.locator("div[role='listbox']")
        listbox.wait_for()

        # Select option
        listbox.locator(".oxd-select-option", has_text=role_name).click()
        
    def select_user_status(self,status):
        dropdown = (
        self.page
        .locator("label:has-text('Status')")
        .locator("xpath=following::div[contains(@class,'oxd-select-text')][1]")
        )
        dropdown.click()
        listbox = self.page.locator("div[role='listbox']")
        listbox.wait_for()

        # Select option
        listbox.locator(".oxd-select-option", has_text=status).click()
        
    
    def enter_employee_name(self, name):
        input_box = self.page.get_by_placeholder("Type for hints...")
        input_box.fill(name)
        option = self.page.locator("div[role='listbox'] >> span", has_text=name)
        option.wait_for()
        option.click()
        

    def enter_username(self, username):
        username_input = self.page.wait_for_selector("//label[text()='Username']/following::input[1]")
        username_input.type(username)

    def enter_password(self, password):
        username_input = self.page.wait_for_selector("//label[text()='Password']/following::input[1]")
        username_input.type(password)

    def enter_confirm_password(self, password):
        username_input = self.page.wait_for_selector("//label[text()='Confirm Password']/following::input[1]")
        username_input.type(password)

    def click_save(self):
        self.page.get_by_role("button", name="Save").click()

    def wait_for_success_toast(self):
        self.page.locator(".oxd-toast-content").wait_for()
    
    def get_error_null_inputs(self):
        errors = self.page.locator(".oxd-input-field-error-message")
        errors.first.wait_for(state="visible")
        return errors.count()

    def test_search_username(self, name):
        username_input = self.page.locator('//label[text()="Username"]/following::input[1]')
        username_input.fill(name)

        # Click Search
        self.page.locator('//button[normalize-space()="Search"]').click()

        # Wait for result
        result = self.page.locator('//span[text()="(1) Record Found"]')
        result.wait_for()

        return result.count()