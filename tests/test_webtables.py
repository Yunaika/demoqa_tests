from selene import have, be
from selene.support.shared import browser

#открываем страницу и скрываем футер
def given_opened_page_webtables():
    browser.open('/webtables')

#добавляем новую строку в таблицу
def test_table_add_new_row():
    # PRECONDITION
    given_opened_page_webtables()

    # WHEN
    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type('Olga')
    browser.element('#lastName').type('Semenova')
    browser.element('#userEmail').type('123@123.ru')
    browser.element('#age').type('30')
    browser.element('#salary').type('5000')
    browser.element('#department').type('Legal')
    browser.element('#submit').click()

    # THEN
    path_to_new_row = '//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@role="rowgroup"][4]//*[@class="rt-td"]'

    browser.element(f'{path_to_new_row}[1]').should(have.exact_text('Olga'))
    browser.element(f'{path_to_new_row}[2]').should(have.exact_text('Semenova'))
    browser.element(f'{path_to_new_row}[3]').should(have.exact_text('30'))
    browser.element(f'{path_to_new_row}[4]').should(have.exact_text('123@123.ru'))
    browser.element(f'{path_to_new_row}[5]').should(have.exact_text('5000'))
    browser.element(f'{path_to_new_row}[6]').should(have.exact_text('Legal'))

#редактируем все поля во второй строке
def test_table_edit_row_two():
    # RECONDITION
    given_opened_page_webtables()
    path_to_row = '//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@role="rowgroup"][2]'
    path_to_column = '//*[@class="rt-td"]'
    path_to_edit_button = '//*[@title="Edit"]'

    # WHEN
    browser.element(path_to_row + path_to_edit_button).click()
    browser.element('#firstName').set_value('Ivan')
    browser.element('#lastName').set_value('Petrov')
    browser.element('#userEmail').set_value('321@123.ru')
    browser.element('#age').set_value('37')
    browser.element('#salary').set_value('2000')
    browser.element('#department').set_value('Legal')
    browser.element('#submit').click()

    # THEN
    browser.element(f'{path_to_row + path_to_column}[1]').should(have.exact_text('Ivan'))
    browser.element(f'{path_to_row + path_to_column}[2]').should(have.exact_text('Petrov'))
    browser.element(f'{path_to_row + path_to_column}[3]').should(have.exact_text('37'))
    browser.element(f'{path_to_row + path_to_column}[4]').should(have.exact_text('321@123.ru'))
    browser.element(f'{path_to_row + path_to_column}[5]').should(have.exact_text('2000'))
    browser.element(f'{path_to_row + path_to_column}[6]').should(have.exact_text('Legal'))

def test_tables_remove_row_three():
    # RECONDITION
    given_opened_page_webtables()

    # WHEN
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@role="rowgroup"][3]//*[@title="Delete"]').click()

    # THEN
    path_to_row = '//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@role="rowgroup"][3]//*[@class="rt-td"]'

    # browser.element(f'{path_to_row}[1]').should(be.empty)
    # browser.element(f'{path_to_row}[2]').should(be.empty)
    # browser.element(f'{path_to_row}[3]').should(be.empty)
    # browser.element(f'{path_to_row}[4]').should(be.empty)
    # browser.element(f'{path_to_row}[5]').should(be.empty)
    # browser.element(f'{path_to_row}[6]').should(be.empty)