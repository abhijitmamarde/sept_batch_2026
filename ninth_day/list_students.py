fp = open("students_names.txt", "r")

students = fp.readlines() 
fp.close()

students = [name.strip() for name in students]
print(f"Students from the batch are: {students}")