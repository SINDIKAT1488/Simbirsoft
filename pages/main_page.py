from .base_page import BasePage
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR,"#login_link")
        login_link.click()

    def authorize(self):
        enter = self.browser.find_element(By.CLASS_NAME,"HeadBanner-Button-Enter")
        enter.click()

        ID = self.browser.find_element(By.ID,"passp-field-login")
        ID.send_keys("S1NDIKAT1488")
        
        enter2 = self.browser.find_element(By.CSS_SELECTOR,"button.Button2")
        enter2.click()

        time.sleep(1)

        password = self.browser.find_element(By.CLASS_NAME,"Textinput-Control")
        password.send_keys("250699rszvqiqeasww")

        submit = self.browser.find_element(By.CSS_SELECTOR,"button[type='submit']")
        submit.click()
    
    def find_messages(self):
        messages = self.browser.find_elements(By.XPATH, "//span[@title='Simbirsoft Тестовое задание']")
        self.message_count = len(messages)
        time.sleep(5)
    
    def send_message(self):
        time.sleep(1)
        send_button = self.browser.find_element(By.CLASS_NAME,"mail-ComposeButton")
        send_button.click()
        time.sleep(1)
        recipient = self.browser.find_element(By.CSS_SELECTOR, ".ComposeRecipients-TopRow .composeYabbles")
        recipient.send_keys("S1NDIKAT1488@yandex.ru")
        subject = self.browser.find_element(By.CSS_SELECTOR, "input.composeTextField")
        subject.send_keys("Simbirsoft Тестовое задание. Зязев")
        message_text = self.browser.find_element(By.CSS_SELECTOR, "div[role='textbox']")
        message_text.send_keys(str(self.message_count))
        send_button2 = self.browser.find_element(By.CSS_SELECTOR, ".ComposeControlPanel-Part button.Button2_view_default")
        send_button2.click()
        time.sleep(5)