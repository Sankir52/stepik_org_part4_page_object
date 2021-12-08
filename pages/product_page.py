#product_page.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        self.should_be_add_product_to_basket()
        self.add_product_to_basket()
        self.check_product_in_basket()

### Алгоритм:
# найти кнопку добавления в корзину
# сохранить назваие товара
# Сохранить стоимость товара
# Нажать кнопку
# Получить из алерта значение и вычислить ответ используя готовый метод solve_quiz_and_get_code()
# ПРОВЕРИТЬ: Сообщение о том, что товар добавлен в корзину.
# ПРОВЕРИТЬ: Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
# ПРОВЕРИТЬ: Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
#

    def should_be_add_product_to_basket(self):
        product_name = self.is_element_present(*ProductPageLocators.PRODUCT_NAME)
        assert product_name, "Не нашли название"
        self.product_name_text = product_name.text
        product_price = self.is_element_present(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price, "Не нашли цену"
        self.product_price_text = product_price.text
        self.add_button = self.is_element_present(*ProductPageLocators.ADD_TO_BASKET)
        assert self.add_button, "Не нашли кнопку"

    def add_product_to_basket(self):
        self.add_button.click()
        self.solve_quiz_and_get_code()

    def check_product_in_basket(self):
        time.sleep(10)
        check_product_name = self.is_element_present(*ProductPageLocators.PRODUCT_NAME_CHECK)
        assert check_product_name, "Не нашли сообщение о добавлении  в корзину"
        check_product_name = check_product_name.text
        assert check_product_name == self.product_name_text, "Название товара не совпало"
        check_product_price = self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_CHECK)
        assert check_product_price , "Не нашли сообения с ценой"
        check_product_price = check_product_price.text
        assert check_product_price == self.product_price_text, "Цена товара не совпала"
