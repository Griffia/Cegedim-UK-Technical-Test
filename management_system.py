import json

with open('students.json') as file:
    student_file = json.load(file)


user_input = input('Please enter the name of the student: ')
user_input = user_input.title()
# Used to format the name similar to the json file

def checking_user():
    for student in student_file['students']:
        if user_input == student['name']:
            print(student['name'])




checking_user()


