import requests
from TOKEN_secret import token


def task_1(geo_logs: list) -> list:
    answer = []
    for dicts in geo_logs:
        if list(dicts.values())[0][1] == "Россия":
            answer.append(dicts)
    return answer


def task_2(ids: dict) -> list:
    answer = []
    for element in ids.values():
        for nums in element:
            answer.append(nums)
    answer = list(set(answer))
    return answer


def task_3(stats: dict) -> list or int:
    answer = []
    for element in stats.items():
        if element[1] == max(stats.values()):
            answer.append(element[0])
    return answer


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def create_folder(self, name_folder):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources?"
        headers = {"Authorization": self.token}
        params = {"path": name_folder}
        response = requests.put(upload_url, headers=headers, params=params)
        return response.status_code

    def exist_folder(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/files"
        headers = {"Authorization": self.token}
        response = requests.get(upload_url, headers=headers)
        return response.text
