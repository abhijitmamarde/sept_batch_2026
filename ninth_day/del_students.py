del_student_name = input("Enter name of student to be deleted:")

# Read existing students
fp = open("students_names.txt", "r")

students = fp.readlines() 
fp.close()

students = [name.strip() for name in students]
# =============

# Assignment
# currently no error / message is displayed if the given 
# student does not already exist. You need to provide
# appropriate message.

# Delete the student with specified name from the students
students = [name for name in students if name != del_student_name]

# Write back the modified students list to file
fp = open("students_names.txt", "w")
fp.writelines([name + "\n" for name in students]) 
fp.close()

print(f"Student with name: {del_student_name} is removed from file!")
