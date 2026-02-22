import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# -------------------------------
# SMOKE TEST
# -------------------------------

@pytest.mark.smoke
def test_valid_login(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate()
    login.login("Admin", "admin123")

    assert dashboard.is_dashboard_loaded(), "Dashboard did not load after valid login"


# -------------------------------
# NEGATIVE LOGIN TESTS
# -------------------------------

@pytest.mark.regression
@pytest.mark.parametrize("username,password", [
    ("WrongUser", "admin123"),
    ("Admin", "WrongPass"),
    ("WrongUser", "WrongPass"),
])
def test_invalid_login(page, username, password):
    login = LoginPage(page)

    login.navigate()
    login.login(username, password)

    error_message = login.get_error_message()
    assert error_message == "Invalid credentials", f"Unexpected error message: {error_message}"


# -------------------------------
# BLANK FIELD VALIDATION
# -------------------------------

@pytest.mark.regression
def test_blank_fields(page):
    login = LoginPage(page)

    login.navigate()
    login.login("", "")

    required_messages = login.get_required_messages()

    assert len(required_messages) == 2, "Both required messages not shown"
    assert "Required" in required_messages[0]
    assert "Required" in required_messages[1]


# -------------------------------
# PASSWORD MASKING
# -------------------------------

@pytest.mark.regression
def test_password_masked(page):
    login = LoginPage(page)

    login.navigate()

    assert login.is_password_masked(), "Password field is not masked"


# -------------------------------
# SQL INJECTION TEST
# -------------------------------

@pytest.mark.regression
def test_sql_injection_login(page):
    login = LoginPage(page)

    login.navigate()
    login.login("' OR '1'='1", "' OR '1'='1")

    assert login.get_error_message() == "Invalid credentials"


# -------------------------------
# XSS ATTACK TEST
# -------------------------------

@pytest.mark.regression
def test_xss_attack(page):
    login = LoginPage(page)

    login.navigate()
    login.login("<script>alert(1)</script>", "test")

    assert login.get_error_message() == "Invalid credentials"


# -------------------------------
# LONG INPUT BOUNDARY TEST
# -------------------------------

@pytest.mark.regression
def test_long_input(page):
    login = LoginPage(page)

    login.navigate()
    long_text = "a" * 300

    login.login(long_text, long_text)

    assert login.get_error_message() == "Invalid credentials"


# -------------------------------
# ENTER KEY LOGIN
# -------------------------------

@pytest.mark.regression
def test_login_with_enter_key(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate()
    login.login_with_enter("Admin", "admin123")

    assert dashboard.is_dashboard_loaded()