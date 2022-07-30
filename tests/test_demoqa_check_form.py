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


def test_submit_form():
    # PRECONDITION
    app.given_opened_practice_form()

    # WHEN
    app.form.set_first_name(user.first_name) \
        .set_last_name(user.last_name) \
        .set_email(user.email) \
        .set_gender(user.gender) \
        .set_mobile_number(user.mobile_number) \
        .set_date_of_birth(user.date_of_birth) \
        .set_subjects(user.subjects) \
        .subjects_should_have(user.subjects) \
        .set_hobbies(user.hobbies) \
        .set_photo(user.photo) \
        .set_current_address(user.current_address) \
        .set_state(user.state) \
        .set_city(user.city) \
        .submit()

    # THEN
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
