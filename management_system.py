import json

with open('students.json') as file:
    student_file = json.load(file)


user_input = input('Please enter the name of the student: ')
user_input = user_input.title()
# Used to format the name similar to the same format as the json file

print('Grades')
print('Attendance')
user_option = input('Please select an option from the options above: ')

user_option = user_option.lower()
# Used to format the users option to the same format as the json file

def checking_user():
    for student in student_file['students']:
        if user_input == student['name']:
            # Check to see if the user input is a valid name in the json file
            if user_option == 'grades':
                # Check to see if the user entered a valid option
                print(f"\n{student['name']}")
                print("\n---Grades---")
                for subject in student['grades']['subjects']:
                    subject_name = subject['name']
                    subject_score = subject['score']
                    print(f"{subject_name} - {subject_score}%")
            elif user_option == 'attendance':
                # Check to see if the user entered a valid option
                print("\n---Attendance---")
                for subject in student['attendance']['subjects']:
                    subject_name = subject['name']
                    subject_attendance = subject['score']
                    print(f"{subject_name} - {subject_attendance}%")
            else:
                print("You did not enter a valid option.")

checking_user()