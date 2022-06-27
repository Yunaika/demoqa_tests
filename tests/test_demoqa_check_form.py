from selene.support.shared import browser
from selene import be, have

#открываем страницу и скрываем футер
def given_opened_text_box_and_hide_footer():
    browser.open('/automation-practice-form')
    browser.element('footer')._execute_script('element.style.display = "None"')

def test_submit_form():
    #открываем страницу и скрываем футер
    given_opened_text_box_and_hide_footer()

    #заполняем обязательные поля формы
    browser.element('#firstName').should(be.blank).type('Olga')
    browser.element('#lastName').should(be.blank).type('Semenova')
    browser.element('#userEmail').should(be.blank).type('123@123.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('[value="1989"]').click()
    browser.element('[value="7"]').click()
    browser.element('[aria-label="Choose Tuesday, August 15th, 1989"]').click()
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    # browser.element('#uploadPicture').type("py.jpg")
    browser.element('#currentAddress').should(be.blank).type('World')
    browser.element('#state').element('#react-select-3-input').type('NCR').press_tab()
    browser.element('#city').element('#react-select-4-input').type('Delhi').press_tab().press_enter()

    #проверяем отправленные данные
    browser.element('//*[@class="table-responsive"]//tr[1]//td[2]')\
        .should(have.text('Olga Semenova'))
    browser.element('//*[@class="table-responsive"]//tr[2]//td[2]') \
        .should(have.text('123@123.ru'))
    browser.element('//*[@class="table-responsive"]//tr[3]//td[2]') \
        .should(have.text('Female'))
    browser.element('//*[@class="table-responsive"]//tr[4]//td[2]') \
        .should(have.text('1234567890'))
    browser.element('//*[@class="table-responsive"]//tr[5]//td[2]') \
        .should(have.text('15 August,1989'))
    browser.element('//*[@class="table-responsive"]//tr[6]//td[2]') \
        .should(have.text('Maths'))
    browser.element('//*[@class="table-responsive"]//tr[7]//td[2]') \
        .should(have.text('Reading'))
    browser.element('//*[@class="table-responsive"]//tr[9]//td[2]') \
        .should(have.text('World'))
    browser.element('//*[@class="table-responsive"]//tr[10]//td[2]') \
        .should(have.text('NCR Delhi'))

