"""
IT Issue Tracking Management System

The script allows users to manage IT Issues
"""

from datetime import datetime

import gspread 
from google.oauth2.service_account import Credentials

SCOPE = [
   "https://www.googleapis.com/auth/spreadsheets",
   "https://www.googleapis.com/auth/drive.file",
   "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file(
    'smartitflow-systemcredentials.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('SmartIT-Flow')


# Increment User_ID by 1 for each entered user issue 

def get_max_id():
    worksheet = SHEET.worksheet('Issue')
    values = worksheet.col_values(1)[2:]  # skip header and User_ID heading
    if not values:
        return 0
    max_id = max(values)
    return int(max_id)


worksheet = SHEET.worksheet('Issue')
issue_id_counter = get_max_id() + 1

issue_description = input("Enter issue description: ")

while True:
    contact_number = input("Enter contact number: ")
    if contact_number.isdigit():
        break
    print("Invalid input. Please enter a number.")

categories = ["Hardware", "Software", "Network", "Other"]
print("IT Issue Category: ")
for i, category in enumerate(categories):
    print(f"{i+1}. {category}")

category_choice = input("Enter the number for the category for the issue: ")
while not category_choice.isdigit() or int(category_choice) < 1 or int(
     category_choice) > len(categories):
    category_choice = input("Invalid input. Enter the category number: ")

chosen_category = categories[int(category_choice)-1]

issue_date_created = datetime.now()

issue_id_formatted = str(issue_id_counter).zfill(3)

worksheet.append_row([
    issue_id_formatted, 
    chosen_category, 
    issue_description, 
    contact_number, 
    issue_date_created.strftime("%d/%m/%Y %H:%M:%S")
])

user_issues = SHEET.worksheet('Issue')

issues = user_issues.get_all_values()

print("Issue ID:", issue_id_formatted)

print("IT Issue category:", chosen_category)

print("User Issue:", issue_description)

print("User Contact Number:", contact_number)

print("IT Issue Date Created:", issue_date_created)

print(issues)