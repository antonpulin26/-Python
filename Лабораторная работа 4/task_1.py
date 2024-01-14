# TODO решите задачу

import json

file_name = "input.json"


def task() -> float:
    with open(file_name) as f:
        json_data = json.load(f)

    result = sum([item["score"] * item["weight"] for item in json_data])
    return round(result, 3)


print(task())
