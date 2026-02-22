import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.test_data import valid_user

@pytest.mark.smoke
def test_valid_login(page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate()
    login.login(valid_user["username"], valid_user["password"])

    assert dashboard.is_dashboard_loaded()