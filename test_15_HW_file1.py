'''
This file checks 3 GET requests with 3 diff status code - 200, 404, 403
'''

import requests

urls = ["https://www.aqa.science/admin/", "https://www.aqa.science/admin1/", "https://www.aqa.science/users/"]


def save_to_file(data: str):
    with open("test.log", "a+") as f:
        f.write(f"{data}\n")


class TestFunctional:

    def setup(self):
        print("\nPre-conditions")

    def teardown(self):
        print(f"\nPost-conditions")

    def setup_class(cls):
        print(f"\nConnect to the internet\n")

    def teardown_class(cls):
        print(f"\nDisconnect from internet")

    def test_admin_page(self):
        response = requests.get(urls[0])
        assert response.status_code == 200, save_to_file(
            f"Failed with code {response.status_code}")
        save_to_file(str(response.status_code))

    def test_admin_page_fail(self):
        response = requests.get(urls[1])
        assert response.status_code == 404
        save_to_file(str(response.status_code))

    def test_admin_not_auth(self):
        response = requests.get(urls[2])
        assert response.status_code == 403
        save_to_file(str(response.status_code))
