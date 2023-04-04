"""
IT Issue Tracking Management System

The script allows users to manage IT Issues
"""

issue_id_counter = 1

issue_description = input("Enter issue description: ")

contact_number = input("Enter contact number: ")

issue_id_formatted = str(issue_id_counter).zfill(2)

if len(issue_id_formatted) == 3:
    issue_id_prefixed = '00' + issue_id_formatted
elif len(issue_id_formatted) == 2:
    issue_id_prefixed = '0' + issue_id_formatted
else:
    issue_id_prefixed = issue_id_formatted

print("Issue ID:", issue_id_counter)

print("User Issue:", issue_description)

print("User Contact Number:", contact_number)