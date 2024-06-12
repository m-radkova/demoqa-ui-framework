from generator import generated_person
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random


class TextBoxPage(BasePage):

    page_url = '/text-box'

    # Input form fields locators
    FULL_NAME = (By.ID, 'userName')
    EMAIL = (By.ID, 'userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress-wrapper #currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress-wrapper #permanentAddress')
    SUBMIT = (By.ID, 'submit')

    # Output form fields locators
    OUTPUT_NAME = (By.CSS_SELECTOR, '#output #name')
    OUTPUT_EMAIL = (By.CSS_SELECTOR, '#output #email')
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

    def fill_all_fields_and_submit(self):
        """Заполняем поля формы рандомными данными, сгенерированными библиотекой Faker"""
        person_info = next(generated_person())
        name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.wait.until(EC.visibility_of_element_located(self.FULL_NAME)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.CURRENT_ADDRESS)).send_keys(current_address)
        self.wait.until(EC.visibility_of_element_located(self.PERMANENT_ADDRESS)).send_keys(permanent_address)
        self.remove_fixedban()
        self.wait.until(EC.visibility_of_element_located(self.SUBMIT)).click()
        return name, email, current_address, permanent_address

    def check_filled_output_form(self):
        """Проверяем, что на нижней форме значения полей соответствуют введённым в верхней"""
        name = self.wait.until(EC.presence_of_element_located(self.OUTPUT_NAME)).text.split(':')[1]
        email = self.wait.until(EC.presence_of_element_located(self.OUTPUT_EMAIL)).text.split(':')[1]
        current_address = \
            self.wait.until(EC.presence_of_element_located(self.OUTPUT_CURRENT_ADDRESS)).text.split(':')[1]
        permanent_address = \
            self.wait.until(EC.presence_of_element_located(self.OUTPUT_PERMANENT_ADDRESS)).text.split(':')[1]
        return name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

    page_url = '/checkbox'

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Collapse all']")
    CHECKED_ITEM_LIST = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    ITEM_TITLE_XPATH = ".//ancestor::span[@class='rct-text']"
    OUTPUT_LIST = (By.CSS_SELECTOR, "span[class='text-success']")

    def expand_all(self):
        """Раскрываем список полностью"""
        self.wait.until(EC.visibility_of_element_located(self.EXPAND_ALL_BUTTON)).click()

    def click_random_checkbox(self):
        """Выбираем несколько рандомных чекбоксов"""
        item_lst = self.wait.until(EC.visibility_of_all_elements_located(self.ITEM_LIST))
        count = 3
        while count >= 0:
            item = item_lst[random.randint(1, 16)]
            self.scroll_to_element(item)
            item.click()
            count -= 1

    def get_titles_of_checked_checkboxes(self):
        """Получаем заголовки кликнутых чекбосков"""
        checked_item_lst = self.wait.until(EC.presence_of_all_elements_located(self.CHECKED_ITEM_LIST))
        data = []
        for item in checked_item_lst:
            title = item.find_element(By.XPATH, self.ITEM_TITLE_XPATH)
            data.append(title.text.lower())
        return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_output_list(self):
        """Получаем список, который отображается в 'You have selected' """
        output_list = self.wait.until(EC.presence_of_all_elements_located(self.OUTPUT_LIST))
        data = []
        for item in output_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):

    page_url = '/radio-button'

    YES_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='yesRadio']")
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='impressiveRadio']")
    NO_RADIO = (By.CSS_SELECTOR, "label[class^='custom-control-label'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

    def click_radio_button(self, choice):
        """Кликаем на выбранный radiobutton"""
        choices = {'Yes': self.YES_RADIO,
                   'Impressive': self.IMPRESSIVE_RADIO,
                   'No': self.NO_RADIO}
        self.remove_footer()
        self.wait.until(EC.visibility_of_element_located(choices[choice])).click()

    def get_output_result(self):
        """Получаем значение из строки 'You have selected...'"""
        return self.wait.until(EC.presence_of_element_located(self.OUTPUT_RESULT)).text


class WebTablesPage(BasePage):

    page_url = '/webtables'

    # Add new person form
    ADD_BUTTON = (By.ID, 'addNewRecordButton')
    FIRST_NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    EMAIL = (By.ID, 'userEmail')
    AGE = (By.ID, 'age')
    SALARY = (By.ID, 'salary')
    DEPARTMENT = (By.ID, 'department')
    SUBMIT_BUTTON = (By.ID, 'submit')

    # Web table
    TABLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.ID, 'searchBox')
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT_XPATH = ".//ancestor::div[@class='rt-tr-group']"

    def add_person(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.wait.until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()
            self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first_name)
            self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last_name)
            self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
            self.wait.until(EC.visibility_of_element_located(self.AGE)).send_keys(age)
            self.wait.until(EC.visibility_of_element_located(self.SALARY)).send_keys(salary)
            self.wait.until(EC.visibility_of_element_located(self.DEPARTMENT)).send_keys(department)
            self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BUTTON)).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_person(self):
        table_list = self.wait.until(EC.presence_of_all_elements_located(self.TABLE_LIST))
        data = []
        for item in table_list:
            data.append(item.text.splitlines())
        return data

    def search_person(self, key_word):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT)).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.wait.until(EC.presence_of_element_located(self.DELETE_BUTTON))
        row = delete_button.find_element(By.XPATH, self.ROW_PARENT_XPATH)
        return row.text.splitlines()
