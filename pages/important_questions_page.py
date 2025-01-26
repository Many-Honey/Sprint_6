from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ImportantQuestionsPage(BasePage):

    # локатор области важных вопросов
    important_questions_area = (By.CLASS_NAME, 'Home_FAQ__3uVm4')


    # метод кликает на вопрос
    def click_on_question(self, question_number):
        self.click_on((By.ID, f'accordion__heading-{question_number}'))

    # метод для ожидания появления ответа
    def wait_for_answer(self, answer_number):
        self.wait_for_element_visible((By.ID, f'accordion__panel-{answer_number}'))

    # метод для получения текста ответа про стоимость и оплату
    def get_answer_text(self, answer_number):
        return self.get_text((By.XPATH, f'.//*[@id="accordion__panel-{answer_number}"]/p'))

