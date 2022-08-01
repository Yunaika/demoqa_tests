import allure
from allure_commons.types import Severity

from demoqa_tests.data import User
from demoqa_tests.model import app

user = User(
    first_name='Olga',
    last_name='Semenova',
    email='123@123.ru',
    gender='Female',
    mobile_number='1234567890',
    date_of_birth='15 August,1989',
    subjects=['Hindi', 'Economics'],
    hobbies=['Sports', 'Reading', 'Music'],
    photo='py.jpg',
    current_address='World',
    state='NCR',
    city='Delhi'
)

@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'juliamur')
@allure.feature('Registration form')
@allure.link('https://demoqa.com', name='Test link')
@allure.title('Successful fill in the form')
def test_submit_form(setup_browser):
    # PRECONDITION
    with allure.step('Open registrations form'):
        browser = setup_browser
        app.given_opened_practice_form(browser)

    # WHEN
    with allure.step(f'Filling user firstname: {user.first_name}'):
        app.form.set_first_name(user.first_name)

    with allure.step(f'Filling user lastname: {user.last_name}'):
        app.form.set_last_name(user.last_name)

    with allure.step(f'Filling user email: {user.email}'):
        app.form.set_email(user.email)

    with allure.step(f'User gender choice: {user.gender}'):
        app.form.set_gender(user.gender)

    with allure.step(f'Filling user mobile number: {user.mobile_number}'):
        app.form.set_mobile_number(user.mobile_number)

    with allure.step(f'Set user date of birth: {user.date_of_birth}'):
        app.form.set_date_of_birth(user.date_of_birth)

    with allure.step(f'Subject choice: {user.subjects}'):
        app.form.set_subjects(user.subjects)
        app.form.subjects_should_have(user.subjects)

    with allure.step(f'Set user hobbies: {user.hobbies}'):
        app.form.set_hobbies(user.hobbies)

    with allure.step(f'Upload user photo: {user.photo}'):
        app.form.set_photo(user.photo)

    with allure.step(f'Filling user current address: {user.current_address}'):
        app.form.set_current_address(user.current_address)

    with allure.step(f'Set user state: {user.state}'):
        app.form.set_state(user.state)

    with allure.step(f'Set user city: {user.city}'):
        app.form.set_city(user.city)

    with allure.step(f'Click Submit'):
        app.form.submit()

    # THEN
    with allure.step("Check form results"):
        app.result.verify_sent_data(user.full_name(user.first_name, user.last_name),
                                    user.email,
                                    user.gender,
                                    user.mobile_number,
                                    user.date_of_birth,
                                    user.subjects,
                                    user.hobbies,
                                    user.photo,
                                    user.current_address,
                                    user.state_and_city(user.state, user.city)
                                    )
