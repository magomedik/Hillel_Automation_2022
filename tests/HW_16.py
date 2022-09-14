"""
CRUD for user via https://www.aqa.science/

"""
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data.locators import LoginPage, AdminPage, CreateUsers, UpdateUsers, FindUsers, DeleteUsers


def test_login(ses_class):
    # Login as admin
    username = pytest.driver.find_element(By.XPATH, LoginPage.username_id)
    password = pytest.driver.find_element(By.XPATH, LoginPage.pswd_id)
    btn = pytest.driver.find_element(By.XPATH, LoginPage.submit_btn)

    username.send_keys(pytest.secret_variables["adm_name"])
    password.send_keys(pytest.secret_variables["adm_password"])
    btn.click()

    # Check login
    adm_page_check = pytest.driver.find_element(By.XPATH, AdminPage.admin_page_header_id)
    assert adm_page_check.text == "Django administration", print("This is not admin page")


def test_create_user():
    # Create user
    add_user = pytest.driver.find_element(By.XPATH, CreateUsers.add_usr_id)
    add_user.click()

    create_username = pytest.driver.find_element(By.XPATH, CreateUsers.username_id)
    create_password = pytest.driver.find_element(By.XPATH, CreateUsers.password_id)
    create_conf_password = pytest.driver.find_element(By.XPATH, CreateUsers.confirm_pswd_id)
    create_save = pytest.driver.find_element(By.XPATH, CreateUsers.save_id)

    create_username.send_keys(pytest.secret_variables["username"])
    create_password.send_keys(pytest.secret_variables["password"])
    create_conf_password.send_keys(pytest.secret_variables["password"])
    create_save.click()

    # Check success of creation
    success_create = pytest.driver.find_element(By.XPATH, CreateUsers.success_id)
    assert success_create.text == pytest.secret_variables["username"], print("User didn't created")
    time.sleep(5)


def test_update_user():
    # Update user
    first_name = pytest.driver.find_element(By.XPATH, UpdateUsers.first_name_id)
    last_name = pytest.driver.find_element(By.XPATH, UpdateUsers.last_name_id)
    save_updates = pytest.driver.find_element(By.XPATH, UpdateUsers.save_btn_id)

    first_name.send_keys(pytest.secret_variables["first_name"])
    last_name.send_keys(pytest.secret_variables["last_name"])
    save_updates.click()

    # Search created user
    time.sleep(5)

    search = pytest.driver.find_element(By.XPATH, FindUsers.find_field_id)

    search.send_keys(pytest.secret_variables["username"])
    search.send_keys(Keys.ENTER)

    search_result = pytest.driver.find_element(By.XPATH, FindUsers.found_username)
    search_result.click()


def test_delete_user():
    # Delete user
    delete_user = pytest.driver.find_element(By.XPATH, DeleteUsers.delete_btn_id)
    delete_user.click()

    confirm_delete = pytest.driver.find_element(By.XPATH, DeleteUsers.confirm_delete_id)
    confirm_delete.click()

    # Check success of deletion
    count_users = pytest.driver.find_element(By.XPATH, DeleteUsers.count_users_id)
    assert count_users.text == '0 users', print("User didn't deleted")
