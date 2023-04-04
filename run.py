"""
IT Issue Tracking Management System

The script allows users to manage IT Issues
"""

issue_id_counter = 1

issue_description = input("Enter issue description: ")

contact_number = input("Enter contact number: ")

issue_id_formatted = str(issue_id_counter).zfill(2)

print("Issue ID:", issue_id_counter)

print("User Issue:", issue_description)

print("User Contact Number:", contact_number)