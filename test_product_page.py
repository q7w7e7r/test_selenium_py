from .pages.product_page import ProductPage

def test_add_product_to_cart(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    assert "promo=newYear" in link, "the link does not contain promo=newYear"
    page = ProductPage(browser,link)
    page.add_product_to_cart()
