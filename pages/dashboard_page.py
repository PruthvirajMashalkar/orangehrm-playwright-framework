from pages.base_page import BasePage

class DashboardPage(BasePage):

    DASHBOARD_HEADER = "h6"

    def is_dashboard_loaded(self):
        return "Dashboard" in self.get_text(self.DASHBOARD_HEADER)