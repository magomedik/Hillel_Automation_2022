'''
This file checks Get and Post requests
'''

import requests
from requests.auth import HTTPBasicAuth
import test_15_HW_file1

urls = ["https://www.aqa.science/users/", "https://www.w3schools.com/python/demopage.php", "https://httpbin.org/post"]


def test_admin_with_cred():
    response = requests.get(urls[0], auth=HTTPBasicAuth("admin", "admin123"))
    assert response.status_code == 200, test_15_HW_file1.save_to_file(
        f"Failed with code {response.status_code}")
    test_15_HW_file1.save_to_file(str(response.status_code))


def test_admin_incorrect_cred():
    response = requests.get(urls[0], auth=HTTPBasicAuth("admin", "admin1234"))
    assert response.status_code == 403
    test_15_HW_file1.save_to_file(str(response.status_code))


def test_post_ex1():
    response = requests.post(urls[1], data={'somekey': 'somevalue'})
    assert response.status_code == 200
    test_15_HW_file1.save_to_file(str(response.status_code))


def test_post_ex2():
    response = requests.post(urls[2], data={'st3': 'jim hopper'})
    assert response.status_code == 200
    test_15_HW_file1.save_to_file(str(response.status_code))
