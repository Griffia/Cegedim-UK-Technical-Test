user_option = user_option.lower()
# # Used to format the users option to the same format as the json file

# def checking_user():
#     for student in student_file['students']:
#         if user_input == student['name']:
#             # Check to see that the user input is a name in the json file
#             if user_option == 'grades':
#                 # Check to see users input option

#                 print(f"\n{student['name']}")
#                 print("\n---Grades---")
#                 for subject in student['grades']['subjects']:
#                     subject_name = subject['name']
#                     subject_score = subject['score']
#                     print(f"{subject_name} - {subject_score}%")
#                     #Formatted string to make the information easier to read

#             elif user_option == 'attendance':
#                     # Check to see users input option
#                 print("\n---Attendance---")
#                 for subject in student['attendance']['subjects']:
#                     subject_name = subject['name']
#                     subject_attendance = subject['score']
#                     print(f"{subject_name} - {subject_attendance}%")
#                     #Formatted string to make the information easier to read
#             else:
#                 print("You did not enter a valid option.")

# checking_user()