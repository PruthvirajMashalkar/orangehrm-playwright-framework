from playwright.sync_api._generated import Page
import pytest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.dashboard_page import DashboardPage

@pytest.mark.smoke
def test_add_user(page: Page):
    admin = AdminPage(page)
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate()
    login.login("Admin", "admin123")

    assert dashboard.is_dashboard_loaded(), "Dashboard did not load after valid login"


    #navigate to admin page
    admin.navigate_to_admin()
    
    #add user
    admin.click_add()
    admin.select_user_role("Admin")
    admin.enter_employee_name("Orange  Test")
    admin.select_user_status("Enabled")
    admin.enter_username("username")
    admin.enter_password("Admin@123")
    admin.enter_confirm_password("Admin@123")
    admin.click_save()
    admin.wait_for_success_toast()
    
@pytest.mark.smoke
def test_add_user_null_inputs(page:Page):
    admin = AdminPage(page)
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate()
    login.login("Admin", "admin123")

    assert dashboard.is_dashboard_loaded(), "Dashboard did not load after valid login"

    #navigate to admin page
    admin.navigate_to_admin()
    
    #add user
    admin.click_add()
    admin.click_save()

    # Wait for validation messages
    page.locator(".oxd-input-field-error-message").first.wait_for(state="visible")

    assert admin.get_error_null_inputs() == 5
    

@pytest.mark.regression
def test_search_users(page:Page):
    admin = AdminPage(page)
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate()
    login.login("Admin", "admin123")

    assert dashboard.is_dashboard_loaded(), "Dashboard did not load after valid login"

    #navigate to admin page
    admin.navigate_to_admin()
    
    admin.test_search_username("Admin") == 1
    
    
    