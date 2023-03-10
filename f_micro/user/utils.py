import requests


def save_user_data_in_dj_micro(data):
    r = requests.post("http://localhost:8002/dj_micro/users/", data=data)
    response = r.json()

    return response
