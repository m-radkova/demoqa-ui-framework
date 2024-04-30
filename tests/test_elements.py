from time import sleep
from pages.elements_page import TextBoxPage
from pages.elements_page import RadioButtonPage


class TestTextBox:
    def test_text_box(self, text_box_page):
        text_box_page.open_page()
        name, email, current_address, permanent_address = text_box_page.fill_all_fields_and_submit()
        output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_output_form()
        assert name == output_name, "name does not match"
        assert email == output_email, "email does not match"
        assert current_address == output_cur_addr, "current address does not match"
        assert permanent_address == output_per_addr, "permanent address does not match"


class TestCheckBox:
    def test_check_box(self, check_box_page):
        check_box_page.open_page()
        check_box_page.expand_all()
        check_box_page.click_random_checkbox()
        input_list = check_box_page.get_titles_of_checked_checkboxes()
        output_list = check_box_page.get_output_list()
        assert input_list == output_list, "the output text does not match the input checkboxes"


class TestRadioButton:
    def test_radio_button(self, radio_button_page):
        choice1, choice2, choice3 = 'Yes', 'Impressive', 'No'
        radio_button_page.open_page()
        radio_button_page.click_radio_button(choice1)
        output_1 = radio_button_page.get_output_result()
        radio_button_page.click_radio_button(choice2)
        output_2 = radio_button_page.get_output_result()
        radio_button_page.click_radio_button(choice3)
        output_3 = radio_button_page.get_output_result()
        assert output_1 == choice1, f'"{choice1}" has not been selected or choice and output text does not match'
        assert output_2 == choice2, f'"{choice2}" has not been selected or choice and output text does not match'
        assert output_3 == choice3, f'"{choice3}" has not been selected or choice and output text does not match'


