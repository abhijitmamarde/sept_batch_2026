fp = open("votedb.txt", "r")

file_records = fp.readlines()
file_records = [row.strip() for row in file_records]
fp.close()

print("File Records are:")
print(file_records)

record = []

for fr in file_records:
    fields = fr.split(",")

    name = fields[0]
    age = int(fields[1])
    # can_vote = bool(fields[2])
    can_vote = True if fields[2] == "True" else False
    
    print(fields)
    print(name, age, can_vote)
    print(type(name), type(age), type(can_vote))
