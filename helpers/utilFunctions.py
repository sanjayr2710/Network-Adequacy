from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import xlrd


class WaitAndAssert:
    @staticmethod
    def assert_and_wait(driver, locator, timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
            assert element is not None
            print("Element found")
        except:
            print("Element not found")

    @staticmethod
    def wait_for_invisibility(driver, locator, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element_located((By.XPATH, locator))
            )
            print("Element is now invisible")
        except TimeoutException:
            print("Element is still visible")


class HardWait:
    @staticmethod
    def hard_wait(seconds):
        time.sleep(seconds)


