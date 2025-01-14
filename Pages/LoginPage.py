import json
import os

import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Base.page_base import PageBase
from Locators.LoginPage import *
from Locators.PEPageLocators import PEPageLocators
from helpers.utilFunctions import WaitAndAssert, HardWait

class LoginPage(PageBase):
    def __init__(self, driver,
                 config_path=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'config.json'))):
        super().__init__(driver)
        self.base_url = self.get_url_from_config(config_path)

    def get_url_from_config(self, config_path):
        try:
            with open(config_path, 'r') as config_file:
                config = json.load(config_file)
            client = config.get("client")

            if client == "Elixir":
                return config.get("ElixirURL", "Elixir URL not found")
            elif client == "BCBSMA":
                return config.get("BCBSMAURL", "BCBSMA URL not found")
            elif client == "Molina":
                return config.get("MolinaURL", "Molina URL not found")
            elif client == "CareSource":
                return config.get("CareSourceURL", "CareSource URl Not found")
            elif client == "Scan":
                return config.get("Scan URL", "Scan URL not found")
            elif client == "Horizon":
                return config.get("Horizon URL not found")
            else:
                raise ValueError("Invalid client specified in config.json")
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {config_path}")
        except Exception as e:
            raise Exception(f"An error occurred while reading the config file: {e}")

    def open(self):
        super().open(self.base_url)

    @allure.step("Login to RA")
    def Login_to_RA(self):
        self.open()
        try:
            config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.json'))
            with open(config_path, 'r') as config_file:
                config = json.load(config_file)
            username = config.get("NA_USERNAME")
            password = config.get("NA_PASSWORD")
        except Exception as e:
            raise Exception(f"Username and Password not found for Client NA: {e}")

        loginEHLogo = LoginLocators.EHlogoLogin
        WaitAndAssert.assert_and_wait(self.driver, loginEHLogo, 10)
        self.driver.find_element(*LoginLocators.user_id).click()
        self.driver.find_element(*LoginLocators.user_id).send_keys(username)
        self.driver.find_element(*LoginLocators.password).click()
        self.driver.find_element(*LoginLocators.password).send_keys(password)
        HardWait.hard_wait(5)
        self.driver.find_element(*LoginLocators.loginButton).click()
        HardWait.hard_wait(5)
        # Check for the force login popup
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, LoginLocators.forceLoginPopUp)))
            self.driver.find_element(By.XPATH, LoginLocators.loginHere).click()
            WaitAndAssert.assert_and_wait(PEPageLocators.ProviderExplorerPageHeading, 10)
        except TimeoutException:

            print("Force login popup not found")


