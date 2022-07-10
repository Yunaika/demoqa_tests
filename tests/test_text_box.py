from selene import have, command
from selene.support.shared import browser

def test_submit_form():
    browser.open('/text-box')
    browser.element('.main-header').should(have.exact_text('Text Box'))
    browser.element('#userName').type('Olga')
    browser.element('#userEmail').type('olgai@test.com')
    browser.element('#submit').perform(command.js.scroll_into_view).click()
