#test_product_page.py
## запуск командой pytest -v -s --tb=line --language=en test_product_page.py

from .pages.product_page import ProductPage

#link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear" #урок 4.3.2
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019" #урок 4.3.3


def test_guest_can_add_product_to_basket(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы — переходим на нужную страницу
    #####page.guest_can_add_product_to_basket()
    param_from_page = page.should_be_add_product_to_basket()
    add_button =param_from_page[0]
    product_name_text= param_from_page[1]
    product_price_text = param_from_page[2]
    page.add_product_to_basket(add_button)
    page.check_product_in_basket(product_name_text,product_price_text)

