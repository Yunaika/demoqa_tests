import pytest
from selene.support.shared import browser

@pytest.fixture(scope='function', autouse=True)
def browser_managment():
     browser.config.base_url = 'https://demoqa.com'
     # browser.config.hold_browser_open = 'True'
     browser.config.window_width = 1600
     browser.config.window_height = 1000