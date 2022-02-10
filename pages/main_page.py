from .base_page import BasePage
from .mail_page import MailPage
from .locators import AuthorizePageLocators
from .test_data import AuthorizePageTestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class AutorizePage(BasePage):

    def authorize(self):
        with allure.step("Авторизация"):

            enter = self.browser.find_element(*AuthorizePageLocators.ENTER)
            enter.click()

            ID = self.browser.find_element(*AuthorizePageLocators.ID)
            ID.send_keys(AuthorizePageTestData.ID)

            enter2 = self.browser.find_element(*AuthorizePageLocators.ENTER2)
            enter2.click()

            time.sleep(1)
            password = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(
                    AuthorizePageLocators.PASSWORD)
            )

            password = self.browser.find_element(
                *AuthorizePageLocators.PASSWORD)
            password.send_keys(AuthorizePageTestData.PASSWORD)

            submit = self.browser.find_element(*AuthorizePageLocators.SUBMIT)
            submit.click()
            return MailPage(browser=self.browser, url=self.browser.current_url)
