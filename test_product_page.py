#test_product_page.py
## запуск командой pytest -v -s --tb=line test_product_page.py
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
#link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear" #урок 4.3.2
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019" #урок 4.3.3
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1" #урок 4.3.6

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def A_test_guest_can_add_product_to_basket(browser, link):
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


# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
def a_test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    param_from_page = page.should_be_add_product_to_basket()
    add_button =param_from_page[0]
    product_name_text= param_from_page[1]
    product_price_text = param_from_page[2]
    page.add_product_to_basket(add_button)
    page.should_not_be_success_message()

# Открываем страницу товара
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
def a_test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()

# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_disappeared
def a_test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    param_from_page = page.should_be_add_product_to_basket()
    add_button =param_from_page[0]
    product_name_text= param_from_page[1]
    product_price_text = param_from_page[2]
    page.add_product_to_basket(add_button)
    page.message_disappeared_after_adding_product_to_basket()


def A_test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def A_test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
# Гость открывает страницу товара
    page = BasketPage(browser, link)
    page.open()
    #page.add_to_basket() # функция добавления в корзину для имитации провала теста по не пустой корзине
# Переходит в корзину по кнопке в шапке
    page.open_basket()
# Ожидаем, что в корзине нет товаров
    page.check_full_basket()
# Ожидаем, что есть текст о том что корзина пуста
    page.check_empty_basket()