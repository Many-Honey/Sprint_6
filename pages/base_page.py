import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    # локатор кнопки "Заказать" в шапке сайта
    order_button_in_header = (By.CSS_SELECTOR, '.Header_Nav__AGCXC > button.Button_Button__ra12g')
    # локатор кнопки "Заказать" в разделе "Как это работает"
    order_button_in_how_it_works_page = (By.CSS_SELECTOR, '.Button_Middle__1CSJM')
    # локатор логотипа Яндекс
    yandex_logo = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    # локатор логотипа Самокат
    scooter_logo = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    # локатор хедера Дзен
    dzen_header = (By.ID, 'dzen-header')

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем станицу {url}")
    # Метод открывает страницу сайта
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Ожидаем, когда {element} станет виден на экране")
    # Метод ожидания появления элемента
    def wait_for_element_visible(self, element):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(element))

    @allure.step("Кликаем на {field_name}")
    # метод кликает на поле
    def click_on(self, field_name):
        self.driver.find_element(*field_name).click()

    @allure.step("Вводим {user_input} в поле {field_name}")
    # метод вводит данные в поле
    def fill_the_field(self, field_name, user_input):
        self.driver.find_element(*field_name).send_keys(user_input)

    # метод кликает на поле и заполняет его
    def click_on_and_fill_the_field(self, field_name, user_input):
        self.click_on(field_name)
        self.fill_the_field(field_name, user_input)

    @allure.step("Скроллим до {locator}")
    # метод скроллит до нужного элемента
    def scroll_to(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидаем, когда откроется страница {url}")
    # метод ждет когда URL поменяется на нужный
    def wait_for_url_changed_to(self, url):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.url_to_be(url))

    @allure.step("Получаем текст {element}")
    # метод получает текст элемента
    def get_text(self, element):
        return self.driver.find_element(*element).text

    # метод переключает драйвер на другую вкладку
    def get_tab_and_switch(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        return tabs





