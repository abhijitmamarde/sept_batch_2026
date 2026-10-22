from csv import DictWriter

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

headers = list(data[0].keys())
headers = [x for x in headers if x != "can_vote"]
print(f"Headers are: {headers}")

with open("votedb_processed.csv", "w") as fp:
    csv = DictWriter(fp, fieldnames=headers)
    csv.writeheader()
    for rec in data:
        if rec["can_vote"] is True:
            del rec["can_vote"]
            csv.writerow(rec)

print("All records are saved to file!")


# Assignment
# list of student names in a class, and has marks for 3 sub: eng, maths, science (out of 100)
# 1. Write CSV records to a file
# 2. Read the CSV records from the file
# 3. Create 3 files CSV (eng_marks.csv...), Top 3 students for that subject Name and marks in that subject

