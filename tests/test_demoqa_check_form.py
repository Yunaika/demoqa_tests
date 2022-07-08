from selene.support.shared import browser
from selene import have, command

from demoqa_tests.controls.checkbox import hobby_select
from demoqa_tests.controls.datepicker import DatePicker
from demoqa_tests.controls.dropdown import Dropdown
from demoqa_tests.controls.table import Table
from demoqa_tests.controls.tags_input import TagsInput
from demoqa_tests.utils import get_abspath, Months


def test_submit_form():
    # PRECONDITION
    given_opened_practice_form()

    # WHEN
    browser.element('#firstName').type('Olga')
    browser.element('#lastName').type('Semenova')
    browser.element('#userEmail').type('123@123.ru')

    gender_female = '[for=gender-radio-2]'
    browser.element(gender_female).click()

    mobile_number = '#userNumber'
    browser.element(mobile_number).type('1234567890')

    calendar = '#dateOfBirthInput'
    browser.element(calendar).click()
    date_of_birth = DatePicker(browser.element('#dateOfBirth'))
    date_of_birth.select_year(1989)
    date_of_birth.select_month(Months.August)
    date_of_birth.select_day(15)
    # date_of_birth.set_date('15 Aug 1989')

    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add('Hindi')
    subjects.add('Econ', autocomplete='Economics')

    hobby_select('Sports')
    hobby_select('Reading')
    hobby_select('Music')

    browser.element('#uploadPicture').send_keys(get_abspath('py.jpg'))

    browser.element('#currentAddress').type('World')

    Dropdown(browser.element('#state')).select(option='NCR')

    Dropdown(browser.element('#city')).autocomplete(option='Delhi')

    browser.element('#submit').perform(command.js.click)

    # THEN
    modal_window = browser.element('.modal-content')
    result_table = Table(modal_window.element('.table'))
    result_table.path_to_cell(row=1, column=2).should(have.exact_text('Olga Semenova'))
    result_table.path_to_cell(row=2, column=2).should(have.exact_text('123@123.ru'))
    result_table.path_to_cell(row=3, column=2).should(have.exact_text('Female'))
    result_table.path_to_cell(row=4, column=2).should(have.exact_text('1234567890'))
    result_table.path_to_cell(row=5, column=2).should(have.exact_text('15 August,1989'))
    result_table.path_to_cell(row=6, column=2).should(have.exact_text('Hindi, Economics'))
    result_table.path_to_cell(row=7, column=2).should(have.exact_text('Sports, Reading, Music'))
    result_table.path_to_cell(row=8, column=2).should(have.exact_text('py.jpg'))
    result_table.path_to_cell(row=9, column=2).should(have.exact_text('World'))
    result_table.path_to_cell(row=10, column=2).should(have.exact_text('NCR Delhi'))


def given_opened_practice_form():
    browser.open('/automation-practice-form')

