from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", \
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru", \
                     help="Choose language: ru or en")
                     help="Choose language: ru or es")

@pytest.fixture(scope="function")
def browser(request):
