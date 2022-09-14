'''
This file describe fixture for pre and post-conditions
'''

import pytest
import os
import time
import json
from selenium import webdriver
from pathlib import Path

# make path runnable on different OS
project_pass = Path.cwd()
file_pass = project_pass.joinpath("data", "cred.json")


@pytest.fixture(scope="session", autouse=True)
def ses_class():
    # Open file with data
    with open(file_pass, "r") as f:
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

# @pytest.fixture(scope="function", autouse=True)
# def setup():
#     print("preconditions")
# def teardown():
#     print("postconditions")
