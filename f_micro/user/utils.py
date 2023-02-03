import requests


def save_user_data_in_dj_micro(data):
    r = requests.post("http://localhost:8001/users/", data=data)
    response = r.json()

    return response
