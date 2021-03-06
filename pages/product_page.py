from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):    
    def product_should_be_added_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADDCART_BUTTON)
        button.click()
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
