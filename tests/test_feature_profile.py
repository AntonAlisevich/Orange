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
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.click_my_info_button()
        self.personal_page.is_opened()
        self.personal_page.change_first_name(f"Test {random.randint(1, 1000)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("Saved Edited name")

    @allure.title("Open Profile page")
    @allure.severity("High")
    @pytest.mark.regression
    def test_open_profile_page(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_login_button()
        self.dashboard_page.click_my_info_button()
        self.personal_page.is_opened()

