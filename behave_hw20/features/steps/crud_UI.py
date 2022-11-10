from behave import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.data.locators import CreateUsers, UpdateUsers, DeleteUsers, FindUsers, AdminPage

use_step_matcher("re")


@given("Via https://www\.aqa\.science/")
def step_impl(context):
    pass


@when("We create a User at https://www\.aqa\.science/")
def step_impl(context):
    # Create user
    add_user = context.driver.find_element(By.XPATH, CreateUsers.add_usr_id)
    add_user.click()

    create_username = context.driver.find_element(By.XPATH, CreateUsers.username_id)
    create_password = context.driver.find_element(By.XPATH, CreateUsers.password_id)
    create_conf_password = context.driver.find_element(By.XPATH, CreateUsers.confirm_pswd_id)
    create_save = context.driver.find_element(By.XPATH, CreateUsers.save_id)

    create_username.send_keys(context.secret_variables["username"])
    create_password.send_keys(context.secret_variables["password"])
    create_conf_password.send_keys(context.secret_variables["password"])
    create_save.click()
    time.sleep(3)

    header_id = context.driver.find_element(By.XPATH, AdminPage.admin_page_header_id)
    header_id.click()
    time.sleep(3)


@then("User was created successfully")
def step_impl(context):
    # reuse code
    context.execute_steps(u"""
    When We tried to find a created User
    Then User was successfully found
    """)


@given("We created a User before")
def step_impl(context):
    pass


@when("We tried to find a created User")
def step_impl(context):
    # Search created user
    time.sleep(2)
    users = context.driver.find_element(By.XPATH, FindUsers.users_id)
    users.click()

    search = context.driver.find_element(By.XPATH, FindUsers.find_field_id)
    search.send_keys(context.secret_variables["username"])
    search.send_keys(Keys.ENTER)

    search_result = context.driver.find_element(By.XPATH, FindUsers.found_username)
    search_result.click()
    time.sleep(3)


@then("User was successfully found")
def step_impl(context):
    # Check success of creation
    success_create = context.driver.find_element(By.XPATH, CreateUsers.success_id)
    assert success_create.text == context.secret_variables["username"], print("User didn't created")


@when("We tried to update a created User")
def step_impl(context):
    # reuse code
    context.execute_steps(u"""
    When We tried to find a created User
    """)

    # Update user
    first_name = context.driver.find_element(By.XPATH, UpdateUsers.first_name_id)
    last_name = context.driver.find_element(By.XPATH, UpdateUsers.last_name_id)
    save_updates = context.driver.find_element(By.XPATH, UpdateUsers.save_btn_id)

    first_name.send_keys(context.secret_variables["first_name"])
    last_name.send_keys(context.secret_variables["last_name"])
    time.sleep(3)
    save_updates.click()


@then("User was successfully updated")
def step_impl(context):
    # go to main amin page
    time.sleep(5)
    header_id = context.driver.find_element(By.XPATH, AdminPage.admin_page_header_id)
    header_id.click()
    time.sleep(5)

    # reuse code
    context.execute_steps(u"""
    When We tried to find a created User
    """)

    first_name = context.driver.find_element(By.XPATH, UpdateUsers.first_name_id).get_attribute("value")

    context.first_name = first_name

    assert context.first_name == 'Magomed', print("User didn't update")


@when("We tried to delete a created User")
def step_impl(context):
    # reuse code
    context.execute_steps(u"""
    When We tried to find a created User
    """)

    # Delete user
    delete_user = context.driver.find_element(By.XPATH, DeleteUsers.delete_btn_id)
    delete_user.click()
    time.sleep(4)

    confirm_delete = context.driver.find_element(By.XPATH, DeleteUsers.confirm_delete_id)
    confirm_delete.click()


@then("User was successfully deleted")
def step_impl(context):
    # Check success of deletion
    count_users = context.driver.find_element(By.XPATH, DeleteUsers.count_users_id)
    assert count_users.text != '0 users', print("User didn't deleted")
