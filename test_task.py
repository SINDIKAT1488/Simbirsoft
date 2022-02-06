from .pages.main_page import MainPage
import allure


@allure.feature('simbirsoft_task')
@allure.story('Авторизация на почте. Поиск и отправка письма')
def test_task_simbirsoft(browser):
  link = "https://mail.yandex.ru/"
  page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
  with allure.step("Открытие страницы"):
    page.open()                      # открываем страницу
  with allure.step("Авторизация"):
    page.authorize()                 # авторизуемся в почте
  with allure.step("Поиск писем"):
    page.find_messages()             # ищем письма
  with allure.step("Отправка письма"):
    page.send_message()              # отправляем письмо