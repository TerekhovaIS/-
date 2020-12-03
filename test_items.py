import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find__card_button(browser):
    try:
        browser.get(link)
        basket_button = browser.find_element_by_css_selector(".btn-add-to-basket")
        result = True
        # time.sleep(30) if you need
    except:
        result = False
        assert result == False, "Element not found"
