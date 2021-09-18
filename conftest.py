import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    language_name = request.config.getoption("language")
    language = None
    if language_name == "en":
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
    elif language_name == "es":
        options.add_experimental_option('prefs', {'intl.accept_languages': "es"})
    elif language_name == "fr":
        options.add_experimental_option('prefs', {'intl.accept_languages': "fr"})
    else:
        raise pytest.UsageError("--language should be en, es or fr")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
