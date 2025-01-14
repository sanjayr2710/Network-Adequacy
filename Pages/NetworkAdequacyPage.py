import time

import allure
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Base.page_base import PageBase
from Locators.LoginPage import *
from Locators.PEPageLocators import *
from Locators.NetworkAdequacyLocators import *
from helpers.utilFunctions import WaitAndAssert, HardWait


class NetworkAdequacyPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on Network Adequacy side menu button")
    def NavigateToNATab(self):
        WaitAndAssert.assert_and_wait(PEPageLocators.ProviderExplorerPageHeading, 10)
        self.driver.find_element(*NetworkAdequacyLocators.NAMenuBtn).click()
        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.NATabHeading, 10)

    @allure.step("Expand Georgia State drop-down")
    def ExpandStateDropDownNATab(self):
        time.sleep(5)
        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.StateGeorgia, 10)
        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.ExpandStateDropdown, 10)
        self.driver.find_element(*NetworkAdequacyLocators.ExpandStateDropdown).click()

    @allure.step("Expand Georgia State drop-down")
    def ScrollDown(self):
        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.firstCheckBox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.firstCheckBox).click()
        self.driver.find_element(*NetworkAdequacyLocators.firstCheckBox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.RICHMOND_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.RICHMOND_county_checkbox).click()
        self.driver.find_element(*NetworkAdequacyLocators.RICHMOND_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.NEWTON_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.NEWTON_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.NEWTON_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.RABUN_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.RABUN_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.RABUN_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.EMANUEL_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.EMANUEL_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.EMANUEL_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.BANKS_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.BANKS_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.BANKS_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.DOUGLAS_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.DOUGLAS_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.DOUGLAS_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.HEARD_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.HEARD_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.HEARD_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.PIKE_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.PIKE_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.PIKE_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.COOK_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.COOK_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.COOK_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.SCHLEY_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.SCHLEY_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.SCHLEY_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.CHATTAHOOCHEE_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.CHATTAHOOCHEE_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.CHATTAHOOCHEE_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.WEBSTER_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.WEBSTER_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.WEBSTER_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.MONROE_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.MONROE_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.MONROE_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.APPLING_county_checkbox, 10)
        # self.driver.find_element(*NetworkAdequacyLocators.APPLING_county).click()
        self.driver.find_element(*NetworkAdequacyLocators.APPLING_county_checkbox).send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    @allure.step("Clicking in found element to navigate to L2 screen")
    def NavigateToL2PageByClickingOnFoundElement(self, xpath):
        HardWait.hard_wait(5)
        retries = 3
        while retries > 0:
            try:
                xpath_to_click = self.driver.find_element(By.XPATH, xpath)
                WaitAndAssert.assert_and_wait(xpath_to_click, 10)
                HardWait.hard_wait(2)
                xpath_to_click.click()
                HardWait.hard_wait(4)
                return
            except (NoSuchElementException, StaleElementReferenceException):
                retries -= 1
                HardWait.hard_wait(2)
                if retries == 0:
                    raise

    @allure.step("Scrolling down until the element visibility")
    def ScrollDownL1Page(self, target_xpath):
        checkpoints = [
            NetworkAdequacyLocators.firstCheckBox,
            NetworkAdequacyLocators.RICHMOND_county_checkbox,
            NetworkAdequacyLocators.NEWTON_county_checkbox,
            NetworkAdequacyLocators.RABUN_county_checkbox,
            NetworkAdequacyLocators.EMANUEL_county_checkbox,
            NetworkAdequacyLocators.BANKS_county_checkbox,
            NetworkAdequacyLocators.DOUGLAS_county_checkbox,
            NetworkAdequacyLocators.HEARD_county_checkbox,
            NetworkAdequacyLocators.PIKE_county_checkbox,
            NetworkAdequacyLocators.COOK_county_checkbox,
            NetworkAdequacyLocators.SCHLEY_county_checkbox,
            NetworkAdequacyLocators.CHATTAHOOCHEE_county_checkbox,
            NetworkAdequacyLocators.WEBSTER_county_checkbox,
            NetworkAdequacyLocators.MONROE_county_checkbox,
            NetworkAdequacyLocators.APPLING_county_checkbox
        ]

        for checkpoint in checkpoints:
            WaitAndAssert.assert_and_wait(checkpoint, 10)

            # Check if the target element is present
            try:
                target_element = self.driver.find_element(By.XPATH, target_xpath)
                if target_element.is_displayed():
                    print(f"Element with xpath {target_xpath} found and clicked.")
                    return
            except NoSuchElementException:
                self.driver.find_element(*checkpoint).send_keys(Keys.PAGE_DOWN)
                time.sleep(1)

        print(f"Element with xpath {target_xpath} not found after scrolling through all checkpoints.")
        time.sleep(3)

    @allure.step("Scrolling down until the element visibility")
    def ScrollDownAndExpandAllDropDown_L2Page(self, target_xpath):
        checkpoints = [
            NetworkAdequacyLocators.firstCheckBoxL2,
            NetworkAdequacyLocators.Mammography_checkbox_c2,
            NetworkAdequacyLocators.Rheumatology_checkbox_c3,
            NetworkAdequacyLocators.VascularSurgery_checkbox_c4
        ]

        for checkpoint in checkpoints:
            WaitAndAssert.assert_and_wait(checkpoint, 10)

            # Check if the target element is present
            try:
                target_element = self.driver.find_element(By.XPATH, target_xpath)
                # target_element2_checkbox = self.driver.find_element(By.XPATH, target_xpath2)
                if target_element.is_displayed():
                    print(f"Element with xpath {target_xpath} found and clicked.")
                    target_element.click()
                    HardWait.hard_wait(5)
                    target_element.click()
                    HardWait.hard_wait(5)
                    WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.AIH_checkbox_L2Page, 20)
                    # time.sleep(5)
                    # target_element2_checkbox.click()
                    # time.sleep(5)
                    # self.ClickOnViewAssociatedProvidersBtn()
                    time.sleep(10)
                    break
            except NoSuchElementException:
                self.driver.find_element(*checkpoint).send_keys(Keys.PAGE_DOWN)
                time.sleep(2)

        print(f"Element with xpath {target_xpath} not found after scrolling through all checkpoints.")
        time.sleep(3)

    def ClickOnViewAssociatedProvidersBtn(self, target_xpath):
        target_element_checkbox = self.driver.find_element(By.XPATH, target_xpath)
        HardWait.hard_wait(10)
        WaitAndAssert.assert_and_wait(target_element_checkbox, 10)
        HardWait.hard_wait(10)
        target_element_checkbox.click()
        HardWait.hard_wait(20)
        try:
            element_btn = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/main/div/div[2]/button")))
            HardWait.hard_wait(5)
            element_btn.click()
        except StaleElementReferenceException:
            HardWait.hard_wait(5)
            element_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div[2]/button")
            element_btn.click()

        HardWait.hard_wait(5)
        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.AddressTypeHeading_L3Page, 10)
        WaitAndAssert.assert_and_wait(NetworkAdequacyLocators.SpecialtyHeaderL2Page_NavigateBack, 10)
        HardWait.hard_wait(5)

        try:
            element_btn = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/main/div/div[1]/p[2]")))
            HardWait.hard_wait(5)
            element_btn.click()
        except StaleElementReferenceException:
            HardWait.hard_wait(20)
            element_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div/div[1]/p[2]")
            element_btn.click()



    @allure.step("Scrolling down until the element visibility ")
    def ScrollDownAndClickOnAllCheckBox_L2Page(self, target_xpath):
        checkpoints = [
            NetworkAdequacyLocators.firstCheckBoxL2,
            NetworkAdequacyLocators.Mammography_checkbox_c2,
            NetworkAdequacyLocators.Rheumatology_checkbox_c3,
            NetworkAdequacyLocators.VascularSurgery_checkbox_c4
        ]

        for checkpoint in checkpoints:
            WaitAndAssert.assert_and_wait(checkpoint, 10)

            # Check if the target element is present
            try:
                target_element_checkbox = self.driver.find_element(By.XPATH, target_xpath)
                if target_element_checkbox.is_displayed():
                    HardWait.hard_wait(10)
                    WaitAndAssert.assert_and_wait(target_element_checkbox, 10)
                    break
            except NoSuchElementException:
                self.driver.find_element(*checkpoint).send_keys(Keys.PAGE_DOWN)
                time.sleep(2)

        print(f"Element with xpath {target_xpath} not found after scrolling through all checkpoints.")
        time.sleep(3)

    def NavigateToL1Page(self):
        try:
            element_btn = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[2]/main/div/div[1]/p[1]")))
            HardWait.hard_wait(5)
            element_btn.click()
        except StaleElementReferenceException:
            HardWait.hard_wait(20)
            element_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div[2]/main/div/div[1]/p[1]")
            element_btn.click()
