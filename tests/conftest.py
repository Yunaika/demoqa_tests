import os
import shutil
import pytest
from dotenv import load_dotenv
from selene import Browser, Config
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from demoqa_tests.utils.attach import add_html, add_screenshot, add_logs, add_video

DEFAULT_BROWSER_VERSION = '100.0'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    shutil.rmtree('allure-results')

    browser.config.base_url = 'https://demoqa.com'
    # browser.config.hold_browser_open = 'True'
    browser.config.window_width = 1600
    browser.config.window_height = 1000

    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
         "browserName": "chrome",
         "browserVersion": browser_version,
         "selenoid:options": {
              "enableVNC": True,
              "enableVideo": True
         }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
         command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
         options=options
    )

    browser.config.driver = driver


    yield browser

    add_html(browser)
    add_screenshot(browser)
    add_logs(browser)
    add_video(browser)
    browser.quit()
