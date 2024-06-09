import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    cookies_qnt = db.select_product_qnt_by_id(4)

    assert cookies_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "тестові", "дані", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


# Individual part of project task"


@pytest.mark.database
def test_check_all_products():
    db = Database()
    products = db.get_all_products_name()

    print(products)


@pytest.mark.database
def test_check_product_quantity():
    db = Database()
    product = db.get__product_quantity_by_name("молоко")

    assert product[0][0] == 10


@pytest.mark.database
def test_check_product_by_nonexists_name():
    db = Database()
    product = db.get__product_quantity_by_name("кефір")

    assert len(product) == 0


@pytest.mark.database
def test_customer_insert():
    db = Database()
    db.insert_customer(3, "Oksana", "Dokivska", "Kyiv", "1111", "Ukraine")
    cust = db.select_customer_by_id(3)

    assert cust[0][0] == "Oksana"
    assert cust[0][1] == "Dokivska"
    assert cust[0][2] == "Kyiv"
    assert cust[0][3] == "1111"
    assert cust[0][4] == "Ukraine"


@pytest.mark.database
def test_name_update():
    db = Database()
    db.update_customer_name_by_id(3, "Olena")
    new_name = db.select_customer_by_id(3)

    assert new_name[0][0] == "Olena"
