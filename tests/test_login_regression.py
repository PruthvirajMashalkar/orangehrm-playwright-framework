import pytest
from pages.login_page import LoginPage
from utils.test_data import invalid_user

@pytest.mark.regression
def test_invalid_login(page):

    login = LoginPage(page)

    login.navigate()
    login.login(invalid_user["username"], invalid_user["password"])

    assert "Invalid credentials" in page.content()