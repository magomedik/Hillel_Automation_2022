import json
import random

import requests
from behave import *
from pathlib import Path

use_step_matcher("re")

# values
headers = {
    'Content-Type': 'application/json'
}
urls = ["https://www.aqa.science/users/"]

# path converter
project_pass = Path.cwd()
add_user_file = project_pass.joinpath("behave_hw20_API//features//added_user.json")
users_list = project_pass.joinpath("tests//users_list.json")


@given("Via https://www\.aqa\.science/")
def step_impl(context):
    pass


@when("We create a User via API")
def step_impl(context):
    # Create user
    payload = json.dumps({
        "username": f"magomed_{random.randint(0, 100)}",
        "email": f"{random.randint(0, 100)}@mgm.com",
        "groups": []
    })
    response = requests.request("POST", urls[0], auth=(context.adm_name, context.adm_pswd), data=payload,
                                headers=headers).json()
    context.res_url = response["url"]

    with open(add_user_file, "w") as f:
        json.dump(response, f)


@then("We should check that user created successfully")
def step_impl(context):
    # check that user created
    assert context.res_url is not None, "User not crested"


@given("We created a User before via API")
def step_impl(context):
    pass


@when("We tried to find a created User via API")
def step_impl(context):
    # read URL value in created user
    with open(add_user_file, "r") as file:
        data = json.load(file)
        data_url = data["url"]
        context.data_url = data_url

    # find created user in users list
    with open(users_list, 'r') as f:
        data = json.load(f)
    value = ""
    for item in data:
        if item.get("url", None) == context.data_url:
            value += item.get("url")
    context.value = value


@then("We should check that user successfully found")
def step_impl(context):
    # check if user founded
    assert context.value == context.data_url, "User not found"


@when("We tried to update a created User via API")
def step_impl(context):
    # read URL value in created user
    with open(add_user_file, "r") as file:
        data = json.load(file)
        data_url = data["url"]
        context.data_url = data_url

    # update created user
    payload = json.dumps({
        "url": context.data_url,
        "username": f"magomed_{random.randint(0, 100)}",
        "email": f"{random.randint(0, 100)}@mgm.com",
        "groups": []
    })
    response = requests.request("PATCH", context.data_url, auth=(context.adm_name, context.adm_pswd), headers=headers,
                                data=payload)
    context.response = response


@then("We should check that user was successfully updated")
def step_impl(context):
    # check that user updated
    assert context.response.status_code == 200, "User not updated"


@when("We tried to delete a created User via API")
def step_impl(context):
    # read URL value in created user
    with open(add_user_file, "r") as file:
        data = json.load(file)
        data_url = data["url"]
        context.data_url = data_url

    # delete created user and erase file added_user.json
    response = requests.request("DELETE", context.data_url, auth=(context.adm_name, context.adm_pswd))
    context.response = response


@then("We should check that user was successfully deleted")
def step_impl(context):
    # check that user deleted
    assert context.response.status_code == 204, "User not deleted"
