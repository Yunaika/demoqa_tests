from selene.support.shared import browser
from selene import be

#открываем страницу и скрываем футер
def given_opened_page_webtables():
    browser.open('/webtables')

#добавляем новую строку в таблицу
def test_table_add_new_row():
    #открываем страницу
    given_opened_page_webtables()

    #добавляем новую строку
    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').should(be.blank).type('Olga')
    browser.element('#lastName').should(be.blank).type('Semenova')
    browser.element('#userEmail').should(be.blank).type('123@123.ru')
    browser.element('#age').should(be.blank).type('30')
    browser.element('#salary').should(be.blank).type('5000')
    browser.element('#department').should(be.blank).type('Legal')
    browser.element('#submit').click()

#редактируем все поля во второй строке
def test_table_edit_row_two():
    #открываем страницу
    given_opened_page_webtables()

    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@role="rowgroup"][2]//*[@title="Edit"]').click()
    browser.element('#firstName').clear().type('Ivan')
    browser.element('#lastName').clear().type('Petrov')
    browser.element('#userEmail').clear().type('321@123.ru')
    browser.element('#age').clear().type('37')
    browser.element('#salary').clear().type('2000')
    browser.element('#department').clear().type('Legal')
    browser.element('#submit').click()

def test_tables_remove_row_three():
    #открываем страницу
    given_opened_page_webtables()

    #удаляем третью строку
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@role="rowgroup"][3]//*[@title="Delete"]').click()