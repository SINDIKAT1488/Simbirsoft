from selenium.webdriver.common.by import By


class AuthorizePageLocators():
    ENTER = (By.CLASS_NAME, "HeadBanner-Button-Enter")
    ID = (By.ID, "passp-field-login")
    ENTER2 = (By.CSS_SELECTOR, "button.Button2")
    PASSWORD = (By.CLASS_NAME, "Textinput-Control")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")


class MailPageLocators():
    MESSAGES = (By.XPATH, "//span[@title='Simbirsoft Тестовое задание']")
    SEND_BUTTON = (By.CLASS_NAME, "mail-ComposeButton")
    RECIPIENTS = (By.CSS_SELECTOR, ".ComposeRecipients-TopRow .composeYabbles")
    SUBJECT = (By.CSS_SELECTOR, "input.composeTextField")
    MESSAGE_TEXT = (By.CSS_SELECTOR, "div[role='textbox']")
    SEND_BUTTON2 = (By.CSS_SELECTOR,
                    ".ComposeControlPanel-Part button.Button2_view_default")
    ALL_MESSAGE_COUNT = (By.CLASS_NAME, "mail-NestedList-Item-Info-Link-Text")
