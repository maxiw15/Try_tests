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
