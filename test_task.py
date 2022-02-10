from .pages.main_page import AutorizePage
from .pages.mail_page import MailPage
import allure


@allure.feature('simbirsoft_task')
@allure.story('Авторизация на почте. Поиск и отправка письма')
def test_task_simbirsoft(browser):
    link = "https://mail.yandex.ru/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    auth_page = AutorizePage(browser, link)
    auth_page.open()                      # открываем страницу
    mail_page = auth_page.authorize()   # авторизуемся в почте
    mail_page.find_messages()             # ищем письма
    mail_page.send_test_message_to_youself()  # отправляем письмо
