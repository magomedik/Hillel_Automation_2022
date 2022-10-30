# -----------------------------------------------------------------------------
# BEHAVE ENVIRONMENT for API tests:
# -----------------------------------------------------------------------------
import json
import requests
from pathlib import Path

# path converter
project_pass = Path.cwd()
add_user_file = project_pass.joinpath("behave_hw20_API//features//added_user.json")
cred = project_pass.joinpath("tests//data//cred.json")
users_list = project_pass.joinpath("tests//users_list.json")


def before_all(context):
    # take admin credentials
    with open(cred, "r") as f:
        secret_variables = json.load(f)
        adm_name = secret_variables["adm_name"]
        adm_pswd = secret_variables["adm_password"]
        context.adm_name = adm_name
        context.adm_pswd = adm_pswd


def after_all(context):
    pass


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def before_tag(context, tag):
    # create users list with all users and write to file
    result = []

    url = 'https://www.aqa.science/'

    response = requests.get(url).json()

    received_url = response['users']

    response_new = requests.get(received_url, auth=(context.adm_name, context.adm_pswd)).json()
    temp_result = response_new["results"]

    result += temp_result

    while True:
        next_url = response_new["next"]
        if not next_url:
            break
        response_new = requests.get(next_url, auth=(context.adm_name, context.adm_pswd)).json()
        result += response_new['results']

    with open(users_list, 'w') as r:
        json.dump(result, r)


def after_tag(context, tag):
    pass
