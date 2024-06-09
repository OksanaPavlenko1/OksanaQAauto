from modules.ui.page_objects.search_page import Search_field
import pytest


@pytest.mark.ui_search
def test_existing_item_page_object():
    search_page = Search_field()
    search_page.go_to()
    search_page.search_item("шампунь")
    search_page.check_url("https://eva.ua/ua/024-104-225/sredstva-mytja-volos")
    search_page.close()
