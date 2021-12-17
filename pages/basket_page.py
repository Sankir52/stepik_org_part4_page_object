from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators
import time
class BasketPage(BasePage):
    def open_basket(self):
        basket_button = self.is_element_present(*BasketPageLocators.BASKET_LINK)
        assert basket_button, "Не нашли корзину"
        basket_button.click()

    def check_full_basket(self):
        basket_full_text = self.is_not_element_present(*BasketPageLocators.BASKET_FULL)
        time.sleep(5)
        assert basket_full_text, "Корзина не пустая"

    def check_empty_basket(self):
        lang_text = self.is_element_present(*BasketPageLocators.LANG_TEXT)
        print("Объект выпадающего списка")
        print(lang_text)
        print("!!Объект выпадающего списка")
        lang_text_value = lang_text.get_attribute("value")
        print("Значение списка")
        print(lang_text_value)
        print("!!Значение списка")
        basket_epmty_text = self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT)
        basket_epmty_text = basket_epmty_text.get_attribute("href")
        print("Ссылка")
        print(basket_epmty_text)
        print("!!Ссылка")
        assert lang_text_value in basket_epmty_text, "нет ссылки пустой корзины"

    # функция добавления в корзину для имитации провала теста по не пустой корзине
    def add_to_basket(self):
        add_button = self.is_element_present(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()
