import json

data = [
    {
        "name": "abhi",
        "age": 18,
        "can_vote": True
    },
    {
        "name": "sagar",
        "age": 17,
        "can_vote": False
    },
    {
        "name": "manish",
        "age": 22,
        "can_vote": True
    },
    {
        "name": "iron man",
        "age": 50,
        "can_vote": False
    },
]

json.dump(
    data,
    open("json_outputted.json", "w")
)

json.dump(
    [x for x in data if x["can_vote"] is True],
    open("can_vote_true.json", "w")
)

json.dump(
    [x for x in data if x["can_vote"] is False],
    open("can_vote_false.json", "w")
)

print("All records are written to JSON file!")

# Assignment Repeat with JSON records for the assignment given in: `csv_writer.py`