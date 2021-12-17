## запуск командой pytest -s -v --tb=line test_main_page.py
# три теста:
# 1. открытие страницы аворизации
# 2. проверка доступности ссылки авторизации.
# 3. Проверка корректности перехода на страницу авторизации и поиск нужных форм.
# Тест №3 реализован с assert, падение теста на первой же неудачной проверке.
import pytest
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        #link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

    def test_guest_should_see_login_link(self,browser):
        #link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()

def A_test_guest_should_see_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
# Гость открывает главную страницу
    page = BasketPage(browser, link)
    page.open()
# Переходит в корзину по кнопке в шапке сайта
    page.open_basket()
# Ожидаем, что в корзине нет товаров
    page.check_full_basket()
# Ожидаем, что есть текст о том что корзина пуста
    page.check_empty_basket()



