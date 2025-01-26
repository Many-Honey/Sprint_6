import allure
import pytest
from selenium import webdriver
from url import *
from data import *


class TestMakeOrderScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('При нажатии на кнопку "Заказать" и заполнении формы заказа валидными данными появляется всплывающее окно с сообщением об успешном создании заказа.')
    @pytest.mark.parametrize('order_button, name, surname, address, station, phone_number, rental_period, scooter_color, comment',
                             make_order_test_data)
    def test_make_order(self, order_button, name, surname, address, station, phone_number, rental_period, scooter_color, comment):
        base_page = BasePage(self.driver)
        base_page.open_page(scooter_main_page)
        base_page.scroll_to(order_button)
        base_page.wait_for_element_visible(order_button)
        base_page.click_on(order_button)
        base_page.wait_for_url_changed_to(scooter_order_page)
        user_info_page = UserInfoOrderPage(self.driver)
        user_info_page.click_on_and_fill_the_field(field_name=UserInfoOrderPage.user_name_field, user_input=name)
        user_info_page.click_on_and_fill_the_field(field_name=UserInfoOrderPage.user_surname_field, user_input=surname)
        user_info_page.click_on_and_fill_the_field(field_name=UserInfoOrderPage.user_address_field, user_input=address)
        user_info_page.fill_the_metro_station_field(station)
        user_info_page.click_on_and_fill_the_field(field_name=UserInfoOrderPage.user_phone_number_field, user_input=phone_number)
        user_info_page.click_on(UserInfoOrderPage.next_button)
        rent_info_page = RentInfoOrderPage(self.driver)
        rent_info_page.wait_for_element_visible(RentInfoOrderPage.rent_info_title)
        rent_info_page.fill_the_delivery_date_field()
        rent_info_page.fill_the_rental_period_field(rental_period)
        rent_info_page.click_on(scooter_color)
        rent_info_page.click_on_and_fill_the_field(field_name=RentInfoOrderPage.comment_field, user_input=comment)
        rent_info_page.click_on(RentInfoOrderPage.order_button)
        rent_info_page.wait_for_element_visible(RentInfoOrderPage.want_to_order_title)
        rent_info_page.click_on(RentInfoOrderPage.yes_button)
        rent_info_page.wait_for_element_visible(RentInfoOrderPage.successful_order_popup)
        actual_successful_order_text = rent_info_page.get_text(RentInfoOrderPage.successful_order_title)
        assert 'Заказ оформлен' in actual_successful_order_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
