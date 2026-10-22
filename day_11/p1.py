import sys
import json

# Input Students
# name, eng, scienc, maths marks (out of 100)

# Option to user:
# 1. To see the topper in a specific subject
# 2. To see the avg of specific student
# 3. To see the class avg of specific subject

student_recs = [
    {'name': 'aaa', 'eng': 11.0, 'sci': 22.0, 'math': 33.0},
    {'name': 'ddd', 'eng': 31.0, 'sci': 32.0, 'math': 44.0},
    {'name': 'bbb', 'eng': 21.0, 'sci': 12.0, 'math': 21.0},
    {'name': 'ccc', 'eng': 31.0, 'sci': 43.0, 'math': 41.0},
]

def get_student_record():
    name = input("Student Name:")
    eng = float(input("Student Marks in English:"))
    sci = float(input("Student Marks in Science:"))
    math = float(input("Student Marks in Maths:"))

    return {
        "name": name,
        "eng": eng,
        "sci": sci,
        "math": math,
    }

# student_rec = get_student_record()
# student_recs.append(student_rec)
# print(student_recs)

def get_top_student(subject_name):
    name = ""

    max = 0
    max_index = 0
    sub_marks = []

    # for index, r in enumerate(student_recs):
    #     mark = r[subject_name]
    #     if max < mark:
    #         max_index = index
    #         max = mark
    #     sub_marks.append(mark)

    sub_marks = sum(get_marks_of_subject(subject_name))

    for index, r in enumerate(student_recs):
        mark = r[subject_name]
        if max < mark:
            max_index = index
            max = mark
    
    print(sub_marks, max, max_index)
    name = student_recs[max_index]["name"]
    return name

# print(get_top_student("math"))
# print(get_top_student("sci"))

def get_marks_of_subject(subject_name):
    marks = []
    for r in student_recs:
        marks.append(r[subject_name])

    return marks

def get_avg_of_class(subject_name):
    subject_marks_sum = sum(get_marks_of_subject(subject_name))
    avg_in_subject = subject_marks_sum / len(student_recs)

    return avg_in_subject

# print(get_avg_of_class("sci"))  # (marks of sci) / (num of Students)
# print(get_avg_of_class("math"))  # (marks of sci) / (num of Students)

def get_avg_of_student(student_name):
    for r in student_recs:
        if student_name == r["name"]:
            return (r["eng"] + r["math"] + r["sci"]) / 3

    raise Exception(f"Student with name: {student_name} Dont's exist!")

# print(get_avg_of_student("aaa"))
# print(get_avg_of_student("bbb"))
# print(get_avg_of_student("ccc"))

def print_menu():
    print("""
    1. Add a new student record.
    2. To see the topper in a specific subject
    3. To see the avg of specific student
    4. To see the class avg of specific subject
    5. Exit
""")
    choice = int(input("Enter your choice:"))
    return choice


# choice = print_menu()
# print(f"Your choice is: {choice}")

def save_records_to_file(student_recs):
    json.dump(student_recs, open("student_records.json", "w"))

def read_records_from_file():
    global student_recs
    try:
        student_recs = json.load(open("student_records.json", "r"))
        print(f"Loaded {len(student_recs)} recs from file!")
    except FileNotFoundError:
        print(f"No Records existed, starting with empty records...")
        student_recs = []

read_records_from_file()

while True:
    choice = print_menu()
    print(f"Your choice is: {choice}")

    if choice == 5:
        save_records_to_file(student_recs)
        sys.exit()
    elif choice == 1:
        student_rec = get_student_record()
        student_recs.append(student_rec)
    elif choice == 2:
        subject_name = input("Enter the subject name:")
        print(f"The name {subject_name} topper is: {get_top_student(subject_name)}")

    ## Assignment implement the other options
    ## Also add options for:
    ## Show the students who have failed in specific subject
    ## Show the student who are failed in ALL subjects
    ## Show the name of student who have scored lowest in speci subject
    ## Show all the existing student records
    ## Delete a specific student record from file/storage
    ## Edit the specific student record - name, marks in any subject