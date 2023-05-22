import requests


def get_resource_groups():
    url = "https://dev.cloud.virtana.com/auth/users"
    response = requests.get(url)
    return response
