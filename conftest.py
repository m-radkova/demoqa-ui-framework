import pytest
from selenium import webdriver
from pages.elements_page import TextBoxPage, RadioButtonPage
from pages.elements_page import CheckBoxPage
from pages.elements_page import WebTablesPage


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture
def text_box_page(driver):
    return TextBoxPage(driver)


@pytest.fixture
def check_box_page(driver):
    return CheckBoxPage(driver)


@pytest.fixture
def radio_button_page(driver):
    return RadioButtonPage(driver)


@pytest.fixture
def web_tables_page(driver):
    return WebTablesPage(driver)
