my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    },
    "brother": {
        "name": "Shane",
        "age": 99
    }
}

for member in my_family:
    print(f"{my_family[member]['name']} is my {member} and is {my_family[member]['age']} years old.")