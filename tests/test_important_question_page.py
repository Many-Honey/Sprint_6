import allure
from selenium import webdriver
from pages.important_questions_page import ImportantQuestionsPage
import pytest
from data import *


class TestImportantQuestionPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка соответствия текста ответа')
    @allure.description('Проверка выпадающего списка в разделе «Вопросы о важном». Проверяем, что при нажатии на стрелочку, открывается соответствующий текст.')
    @pytest.mark.parametrize('question_number, answer_number, expected_answer',
                             important_question_test_data)
    def test_click_question_answer_text(self, question_number, answer_number,
                                                                  expected_answer):
        important_questions_page = ImportantQuestionsPage(self.driver)
        important_questions_page.open_page('https://qa-scooter.praktikum-services.ru/')
        important_questions_page.scroll_to(ImportantQuestionsPage.important_questions_area)
        important_questions_page.click_on_question(question_number)
        important_questions_page.wait_for_answer(answer_number)
        actual_answer_text = important_questions_page.get_answer_text(answer_number)
        assert actual_answer_text == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
