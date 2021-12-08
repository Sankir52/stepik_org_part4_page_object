from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #registration_link   #login_link

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class,'product_main')]//h1[1]")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class,'product_main')]//p[1]")
    PRODUCT_NAME_CHECK = (By.XPATH, "//div[@id='messages']//strong[1]")
    PRODUCT_PRICE_CHECK = (By.XPATH, "//div[@id='messages']//div[3]//strong[1]")

