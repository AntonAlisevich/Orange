import random
import allure
import pytest
import time
from base.base_test import BaseTest


@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change Profile first name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login_button()
        self.dashboard_page.click_my_info_button()
        self.personal_page.is_opened()
        time.sleep(5)
        self.personal_page.change_first_name(f"Test {random.randint(1, 1000)}")
        time.sleep(5)
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("Saved Edited name")



