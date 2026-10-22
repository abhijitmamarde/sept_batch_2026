from csv import DictReader

# # Sample for read data
# data = [
#     {
#         "name": "abhi",
#         "age": 18,
#         "can_vote": True
#     },
#     {
#         "name": "sagar",
#         "age": 17,
#         "can_vote": False
#     },
#     {
#         "name": "manish",
#         "age": 22,
#         "can_vote": True
#     },
#     {
#         "name": "iron man",
#         "age": 50,
#         "can_vote": False
#     },
# ]

data = []
with open("votedb.csv", "r") as fp:
    csv = DictReader(fp)
    for row in csv:
        # print(row)
        row["age"] = int(row["age"])
        row["can_vote"] = True if row["can_vote"] == "True" else False

        data.append(row)



# Benefit once we have this data structure/format
# List of Dict Records
for d in data:
    name = d["name"]
    if d["can_vote"] is True:
        print(f"Person {name} can vote!")
