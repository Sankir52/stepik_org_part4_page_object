#test_product_page.py
## запуск командой pytest -v -s --tb=line --language=en test_product_page.py

from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы — переходим на нужную страницу
    page.guest_can_add_product_to_basket()
    #time .sleep(5)
    # получаем текущий url из браузера
    #login_page = ProductPage(browser, browser.current_url)
    # выполняем метод на новой странице
    #login_page.should_be_login_page()
