from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RentInfoOrderPage(BasePage):

    # локатор заголовка "Про аренду"
    rent_info_title = (By.XPATH, '//div[text()="Про аренду"]')
    # локатор поля Когда привезти самокат
    delivery_date_field = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    # локатор всплывающего календаря
    date_piker = (By.CLASS_NAME, 'react-datepicker__month-container')
    # локатор кнопки "следующий месяц"
    next_month_button = (By.XPATH, '//button[text()="Next Month"]')
    # локатор первого числа месяца
    first_day_of_month = (By.XPATH, '//div[text()="1"]')
    # локатор поля Срок аренды
    rental_period_field = (By.CSS_SELECTOR, '.Dropdown-root')
    # локатор для выпадающего списка со сроками аренды
    rental_period_dropdown_list = (By.CLASS_NAME, 'Dropdown-menu')
    # локатор срока аренды "двое суток"
    two_days_rent_period = (By.XPATH, '//div[text()="двое суток"]')
    # локатор срока аренды "семеро суток"
    seven_days_rent_period = (By.XPATH, '//div[text()="семеро суток"]')
    # локатор чек бокса "черный жемчуг"
    black_scooter_color = (By.ID, 'black')
    # локатор чек бокса "серая безысходность"
    grey_scooter_color = (By.ID, 'grey')
    # локатор поля Комментарий
    comment_field = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    # локатор кнопки Заказать
    order_button = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    # локатор заголовка "Хотите оформить заказ?" во всплывающем окне подтверждения заказа
    want_to_order_title = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    # локатор кнопки "Да" во всплывающем окне подтверждения заказа
    yes_button = (By.XPATH, '//button[text()="Да"]')
    # локатор всплывающего окна уведомления об успешно оформленном заказе
    successful_order_popup = (By.CLASS_NAME, 'Order_Modal__YZ-d3')
    # локатор заголовка "Заказ оформлен"
    successful_order_title = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')


    # метод заполняет поле даты доставки выбирая дату из всплывающего календаря
    def fill_the_delivery_date_field(self):
        # кликаем по полю даты доставки
        self.click_on(self.delivery_date_field)
        # ждем пока появится всплывающий календарь
        self.wait_for_element_visible(self.date_piker)
        # жмем кнопку "следующий месяц"
        self.click_on(self.next_month_button)
        # выбираем 1ое число
        self.click_on(self.first_day_of_month)

    # метод заполняет поле Срок аренды
    def fill_the_rental_period_field(self, rental_period):
        # кликаем по полю срока аренды
        self.click_on(self.rental_period_field)
        # ждем пока появится выпадающий список
        self.wait_for_element_visible(self.rental_period_dropdown_list)
        # скроллим до нужного периода аренды
        self.scroll_to(rental_period)
        # кликаем на нужный период аренды
        self.click_on(rental_period)








