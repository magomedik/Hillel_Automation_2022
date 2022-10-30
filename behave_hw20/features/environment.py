# -----------------------------------------------------------------------------
# BEHAVE ENVIRONMENT for UI tests:
# -----------------------------------------------------------------------------
import os
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.data.locators import LoginPage, AdminPage
from pathlib import Path

# make path runnable on different OS
project_pass = Path.cwd()
file_pass = project_pass.joinpath("data", "cred.json")
add_user_file = project_pass.joinpath("added_user.json")


def before_all(context):
    # Open file with data
    with open('/Users/cityman88/PycharmProjects/Hillel/tests/data/cred.json', "r") as f:
        secret_variables = json.load(f)

    # Run container
    port = 4488

    # for run docker local on M1
    os.system(f"docker run -d --name mgm_seleniarm_chrome -p {port}:4444 -p 5900:5900 seleniarm/standalone-chromium")

    # for run docker local on Jenkins on other process
    # os.system(f"docker run -d --name mgm_seleniarm_chrome -p {port}:4444 selenium/standalone-chrome-debug")
    time.sleep(3)

    # Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    # Run Chrome with options
    driver = webdriver.Remote(
        command_executor=f'http://localhost:{port}/wd/hub',
        options=options
    )

    # open url
    driver.get(secret_variables["endpoint"])
    context.driver = driver
    context.secret_variables = secret_variables


def after_all(context):
    # Post-conditions
    time.sleep(3)
    context.driver.close()
    os.system("docker rm --force mgm_seleniarm_chrome")


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_scenario(context, scenario):
    # Login as admin
    username = context.driver.find_element(By.XPATH, LoginPage.username_id)
    password = context.driver.find_element(By.XPATH, LoginPage.pswd_id)
    btn = context.driver.find_element(By.XPATH, LoginPage.submit_btn)

    username.send_keys(context.secret_variables["adm_name"])
    password.send_keys(context.secret_variables["adm_password"])
    btn.click()


def after_scenario(context, scenario):
    # logout
    time.sleep(3)
    logout = context.driver.find_element(By.XPATH, AdminPage.logout_id)
    logout.click()
    time.sleep(3)
    log_again = context.driver.find_element(By.XPATH, AdminPage.log_again_id)
    log_again.click()


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass
