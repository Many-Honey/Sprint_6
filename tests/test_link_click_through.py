import allure
from selenium import webdriver
from pages.base_page import BasePage
from url import *



class TestLinkClickThrough:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Нажатие на лого Яндекс ведет на страницу Дзена')
    @allure.description('При нажатии на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_click_yandex_logo_leads_to_dzen_page(self):
        base_page = BasePage(self.driver)
        base_page.open_page(scooter_main_page)
        base_page.wait_for_element_visible(BasePage.yandex_logo)
        base_page.click_on(BasePage.yandex_logo)
        base_page.get_tab_and_switch()
        base_page.wait_for_element_visible(BasePage.dzen_header)
        assert 'https://dzen.ru/' in self.driver.current_url

    @allure.title('Нажатие на лого Самокат ведет на главную страницу "Самоката"')
    def test_click_scooter_logo_leads_to_main_page(self):
        base_page = BasePage(self.driver)
        base_page.open_page(scooter_main_page)
        base_page.click_on(BasePage.order_button_in_header)
        base_page.click_on(BasePage.scooter_logo)
        assert self.driver.current_url == scooter_main_page


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()