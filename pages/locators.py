from selenium.webdriver.common.by import By
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class BasketPageLocators():
    BASKET_LINK = (By.XPATH, "//div[contains(@class,'basket-mini')]//a[1]")
    BASKET_EMPTY_TEXT = (By.XPATH, "//div[@id='content_inner']//p[1]/a[1]")
    BASKET_FULL = (By.XPATH, "//div[@class='row']//h2[contains(@class, 'col-sm-6')]")
    LANG_TEXT = (By.XPATH, "//select[@name='language']//option[@selected]")
class ProductPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class,'product_main')]//h1[1]")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class,'product_main')]//p[1]")
    PRODUCT_NAME_CHECK = (By.XPATH, "//div[@id='messages']//strong[1]")
    PRODUCT_PRICE_CHECK = (By.XPATH, "//div[@id='messages']//div[3]//strong[1]")

