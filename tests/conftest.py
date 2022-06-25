import pytest
from selene.support.shared import browser

@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    browser.config.base_url = 'https://demoqa.com/'