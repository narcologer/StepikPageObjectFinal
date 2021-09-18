from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_add_to_cart(browser):
    page=ProductPage(browser,link)
    page.open()
    page.product_should_be_added_to_cart()
