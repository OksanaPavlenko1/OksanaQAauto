from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class Search_field(BasePage):
    URL = "https://eva.ua/ua"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(Search_field.URL)

    def search_item(self, item_name):
        search_elem = self.driver.find_element(By.CLASS_NAME, "m-search-bar__input")
        search_elem.send_keys(item_name)
        search_btn_elem = self.driver.find_element(
            By.CLASS_NAME, "m-search-bar__button"
        )
        search_btn_elem.click()

    def check_url(self, expected_url):
        return self.driver.current_url == expected_url
