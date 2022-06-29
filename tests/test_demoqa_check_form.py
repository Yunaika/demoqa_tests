from selene.support.shared import browser
from selene import have, command
from demoqa_tests.utils import get_abspath

def test_submit_form():
    # PRECONDITION
    given_opened_text_box()

    # WHEN
    browser.element('#firstName').type('Olga')
    browser.element('#lastName').type('Semenova')
    browser.element('#userEmail').type('123@123.ru')

    gender_female = '[for=gender-radio-2]'
    browser.element(gender_female).click()

    mobile_number = '#userNumber'
    browser.element(mobile_number).type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('#dateOfBirth').element('[value="1989"]').click()
    browser.element('#dateOfBirth').element('[value="7"]').click()
    browser.element('#dateOfBirth').element('[aria-label="Choose Tuesday, August 15th, 1989"]').click()

    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Reading')).click()

    browser.element('#uploadPicture').send_keys(get_abspath('py.jpg'))

    browser.element('#currentAddress').type('World')
    browser.element('#state').element('#react-select-3-input').type('NCR').press_tab()
    browser.element('#city').element('#react-select-4-input').type('Delhi').press_tab()

    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element(path_to_cell(1, 2)).should(have.exact_text('Olga Semenova'))
    browser.element(path_to_cell(2, 2)).should(have.exact_text('123@123.ru'))
    browser.element(path_to_cell(3, 2)).should(have.exact_text('Female'))
    browser.element(path_to_cell(4, 2)).should(have.exact_text('1234567890'))
    browser.element(path_to_cell(5, 2)).should(have.exact_text('15 August,1989'))
    browser.element(path_to_cell(6, 2)).should(have.exact_text('Maths'))
    browser.element(path_to_cell(7, 2)).should(have.exact_text('Reading'))
    browser.element(path_to_cell(8, 2)).should(have.exact_text('py.jpg'))
    browser.element(path_to_cell(9, 2)).should(have.exact_text('World'))
    browser.element(path_to_cell(10, 2)).should(have.exact_text('NCR Delhi'))


def given_opened_text_box():
    browser.open('/automation-practice-form')

def path_to_cell(tr, td):
    return f'//*[@class="table-responsive"]//tr[{tr}]//td[{td}]'