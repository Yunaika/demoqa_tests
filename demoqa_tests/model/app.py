import time

from selene.support.shared import browser

from demoqa_tests.model.pages.student_registration_page import StudentRegistrationForm, ModalDialogSubmittingForm

form = StudentRegistrationForm()
result = ModalDialogSubmittingForm()


def given_opened_practice_form():
   browser.open('https://demoqa.com/automation-practice-form')
   time.sleep(1)