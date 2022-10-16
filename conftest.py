'''
This file describe all direct fixtures and pre/post-conditions fixture
'''

import pytest
import os
import time
import json

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.data.locators import LoginPage, AdminPage, FindUsers
from pathlib import Path

# make path runnable on different OS
project_pass = Path.cwd()
file_pass = project_pass.joinpath("data", "cred.json")
add_user_file = project_pass.joinpath("added_user.json")


@pytest.fixture(scope="session", autouse=True)
def ses_class():
    # Open file with data
    with open(file_pass, "r") as f:
        pytest.secret_variables = json.load(f)

    # Run container
    port = 4444

    # for run docker local on M1
    # os.system(f"docker run -d --name mgm_seleniarm_chrome -p {port}:4444 -p 5900:5900 seleniarm/standalone-chromium")

    # for run docker local on Jenkins on other process
    os.system(f"docker run -d --name mgm_seleniarm_chrome -p 4444:4444  -p 5900:5900 selenium/standalone-chrome")
    time.sleep(20)

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


@pytest.fixture()
def user_data():
    # read URL value in created user
    with open(add_user_file, "r") as f:
        data = json.load(f)
        data_url = data["url"]
        return data_url


@pytest.fixture()
def cred_file():
    # take admin credentials
    with open(file_pass, "r") as f:
        secret_variables = json.load(f)
        adm_name = secret_variables["adm_name"]
        adm_pswd = secret_variables["adm_password"]
        return adm_name, adm_pswd


@pytest.fixture()
def check_user(cred_file):
    # create users list with all users and write to file
    result = []

    url = 'https://www.aqa.science/'

    response = requests.get(url).json()

    received_url = response['users']

    response_new = requests.get(received_url, auth=cred_file).json()
    temp_result = response_new["results"]

    result += temp_result

    while True:
        next_url = response_new["next"]
        if not next_url:
            break
        response_new = requests.get(next_url, auth=cred_file).json()
        result += response_new['results']

    with open('users_list.json', 'w') as r:
        json.dump(result, r)

# @pytest.fixture(scope="function", autouse=True)
# def setup():
#     print("preconditions")
# def teardown():
#     print("postconditions")
