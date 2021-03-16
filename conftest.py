from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption('--language',action='store',default="en",help='Enter language in command line, please')
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    language=request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    print("\nstart browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()

