from .base_page import BasePage
from .locators import MailPageLocators
from .test_data import MailPageTestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MailPage(BasePage):
    def find_messages(self):
        with allure.step("Поиск писем"):
            self.browser.implicitly_wait(5)
            messages = self.browser.find_elements(*MailPageLocators.MESSAGES)
            print(len(messages))
            self.message_count = len(messages)

    def send_test_message_to_youself(self):
        with allure.step("Отправка письма"):

            send_button = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(MailPageLocators.SEND_BUTTON)
            )
            send_button.click()
            recipient = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(MailPageLocators.RECIPIENTS)
            )
            recipient.send_keys(MailPageTestData.RECIPIENTS)
            subject = self.browser.find_element(*MailPageLocators.SUBJECT)
            subject.send_keys(MailPageTestData.SUBJECT)
            message_text = self.browser.find_element(
                *MailPageLocators.MESSAGE_TEXT)
            message_text.send_keys(str(self.message_count))
            all_message_count_before = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(
                    MailPageLocators.ALL_MESSAGE_COUNT)
            )
            all_message_count_before_text = all_message_count_before.text
            send_button2 = self.browser.find_element(
                *MailPageLocators.SEND_BUTTON2)
            send_button2.click()
            self.browser.refresh()
            confirm = self.browser.switch_to.alert
            confirm.accept()
            # time.sleep(5)
            all_message_count_after = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(
                    MailPageLocators.ALL_MESSAGE_COUNT)
            )
            all_message_count_after_text = all_message_count_after.text
            print(all_message_count_before_text)
            print(all_message_count_after_text)
            assert all_message_count_before_text != all_message_count_after_text, "Письмо не отправилось"
