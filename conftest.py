'''
This file describe fixture for pre and post-conditions
'''

import pytest
import os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data.locators import LoginPage, AdminPage, FindUsers
from pathlib import Path


# make path runnable on different OS
# project_pass = Path.cwd()
# file_pass = project_pass.joinpath("data", "cred.json")

@pytest.fixture(scope="session", autouse=True)
def ses_class():
    # Open file with data
    with open('/Users/cityman88/PycharmProjects/Hillel/data/cred.json', "r") as f:
        pytest.secret_variables = json.load(f)

    # Run container
    os.system("docker run -d --name mgm_seleniarm_chrome -p 4444:4444 -p 5900:5900 seleniarm/standalone-chromium")
    time.sleep(3)

    # Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    # Run Chrome with options
    pytest.driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    # open url
    pytest.driver.get(pytest.secret_variables["endpoint"])
    yield
    # Post-conditions
    time.sleep(3)
    pytest.driver.close()
    os.system("docker rm --force mgm_seleniarm_chrome")


@pytest.fixture(scope="function", autouse=True)
def login_logout_func():
    # Login as admin
    username = pytest.driver.find_element(By.XPATH, LoginPage.username_id)
    password = pytest.driver.find_element(By.XPATH, LoginPage.pswd_id)
    btn = pytest.driver.find_element(By.XPATH, LoginPage.submit_btn)

    username.send_keys(pytest.secret_variables["adm_name"])
    password.send_keys(pytest.secret_variables["adm_password"])
    btn.click()
    yield
    # logout
    logout = pytest.driver.find_element(By.XPATH, AdminPage.logout_id)
    logout.click()
    time.sleep(2)
    log_again = pytest.driver.find_element(By.XPATH, AdminPage.log_again_id)
    log_again.click()


@pytest.fixture()
def find_func():
    # Search created user
    time.sleep(2)
    users = pytest.driver.find_element(By.XPATH, FindUsers.users_id)
    users.click()

    search = pytest.driver.find_element(By.XPATH, FindUsers.find_field_id)
    search.send_keys(pytest.secret_variables["username"])
    search.send_keys(Keys.ENTER)

    search_result = pytest.driver.find_element(By.XPATH, FindUsers.found_username)
    search_result.click()
    time.sleep(3)

# @pytest.fixture(scope="function", autouse=True)
# def setup():
#     print("preconditions")
# def teardown():
#     print("postconditions")
