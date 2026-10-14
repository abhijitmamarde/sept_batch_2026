name = input("Enter name:")
age = int(input("Enter age:"))
can_vote = True if (age >= 18) else False

fp = open("votedb.txt", "a")
fp.write(f"{name},{age},{can_vote}\n")
fp.close()
