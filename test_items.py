import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contains_add_to_cart_button(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
    # time.sleep(30) if you need
    assert True, "Add to cart button not found"
