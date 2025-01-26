from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserInfoOrderPage(BasePage):

    # локатор заголовка "Для кого самокат"
    user_info_title = (By.XPATH, '//div[text()="Для кого самокат"]')
    # локатор поля Имя
    user_name_field = (By.XPATH, '//input[@placeholder="* Имя"]')
    # локатор поля Фамилия
    user_surname_field = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    # локатор поля Адрес
    user_address_field = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    # локатор поля Станция метро
    user_metro_station_field = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    # локатор поля Телефон
    user_phone_number_field = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    # локатор для комбобокса станции метро
    metro_station_combo_box = (By.CLASS_NAME, 'select-search__select')
    # локатор станции Алексеевская
    alexeevskaya_station = (By.XPATH, '//li[@data-index="84"]')
    # локатор станции Курская
    kurskaya_station = (By.XPATH, '//li[@data-index="58"]')
    # локатор кнопки Далее
    next_button = (By.XPATH, '//button[text()="Далее"]')


    # метод заполняет поле Станция метро выбирая из списка нужную станцию
    def fill_the_metro_station_field(self, station):
        # кликаем по полю Станция метро
        self.click_on(self.user_metro_station_field)
        # ждем пока появится комбобокс со станциями
        self.wait_for_element_visible(self.metro_station_combo_box)
        # скроллим до нужной станции
        self.scroll_to(station)
        # кликаем на нужную станцию метро
        self.click_on(station)







