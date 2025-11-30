import json

employees = {
    "id-01": {
        "name": "John",
        "age": 23,
        "info":
            {"os": "osx", "type": "hooligan"}
    },
    "id-02": {
        "name": "Mark",
        "age": 25,
        "info":
            {"os": "linux", "type": "historian"}
    },
    "id-03": {
        "name": "Fedor",
        "age": 43,
        "info":
            {"os": "linux", "type": "hooligan"}
    },
    "id-04": {
        "name": "Dug",
        "age": 35,
        "info":
            {"os": "windows", "type": "historian"}
    }
}


class Employee:

    def __init__(self, name, age, info):
        self.name = name
        self.age = age
        self.info = info


class Info:
    def __init__(self, os, type):
        self.os = os
        self.type = type


emp_dict = json.loads(employees)



