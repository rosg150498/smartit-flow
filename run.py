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


# Updating cell heading to D1 and E1 to Google Sheets to Issue sheet
worksheet = SHEET.worksheet('Issue')
worksheet.add_cols(2)
worksheet.update_cell(1, 4, 'Forename')
worksheet.update_cell(1, 5, 'Surname')

# Increment User_ID by 1 for each entered user issue 


def get_max_id():
    worksheet = SHEET.worksheet('Issue')
    values = worksheet.col_values(1)[2:]  # skip header and User_ID heading
    if not values:
        return 0
    max_id = max(values)
    return int(max_id)


def search_issues(search_term):
    values = SHEET.worksheet('Issue').get_all_values()

    matching_rows = [
        row for row in values[1:] if
        search_term.lower() in (row[0].lower(),
                                row[3].lower())]

    for row in matching_rows:
        print(row)


chosen_category = ''
issue_description = ''
contact_number = ''
issue_date_created = ''
issue_id_formatted = ''


def add_issue():
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

    category_choice = input("Enter the number for the category for the issue:")
    while not category_choice.isdigit() or int(category_choice) < 1 or int(
         category_choice) > len(categories):
        category_choice = input("Invalid input. Enter the category number: ")

    chosen_category = categories[int(category_choice)-1]

    issue_date_created = datetime.now()

    issue_id_formatted = str(issue_id_counter).zfill(3)

    worksheet = SHEET.worksheet('Issue')
    worksheet.append_row([
        issue_id_formatted, 
        chosen_category, 
        issue_description, 
        contact_number, 
        issue_date_created.strftime("%d/%m/%Y %H:%M:%S")
    ])

    print("Issue has been added successfully!")


issue_id_formatted = issue_id_formatted
chosen_category = chosen_category
issue_description = issue_description
contact_number = contact_number
issue_date_created = issue_date_created


def update_user():

    user_id = input("Enter the User ID of the user you want to update:")

    worksheet = SHEET.worksheet('Issue')
    user_rows = worksheet.get_all_values()
    user_row = None
    for row in user_rows[1:]:
        if row[0] == user_id: 
            user_row = row
            break
    if user_row is None:
        print(f"No user found with ID {user_id}.")
        return 

    print(f"Current results for user {user_id}:")
    print(f"Category: {user_row[2]}")
    print(f"Issue Description: {user_row[3]}")
    print(f"Forename: {user_row[4]}")
    print(f"Surname: {user_row[5]}")
    print(f"Contact Number: {user_row[6]}")


# Define a function to edit the issue sheet
def edit_sheet():
    row_num = input('Enter the row number you want to edit: ')
    col_num = input('Enter the column number you want to edit: ')
    new_value = input('Enter the new value you want to set: ')
    worksheet.update_cell(row_num, col_num, new_value)
    print('Value updated successfully.')


edit_sheet()


# Call the edit_sheet() function to make changes to the sheet
edit_sheet()

while True:
    action = input('Enter action (search / add / update / delete / quit): ')

    if action == 'search':
        search_term = input('Enter search term: ')
        search_issues(search_term)

    elif action == 'add issue':
        add_issue()

    elif action == 'update':
        update_user()

    elif action == 'delete':
        user_id = input("Enter the User ID of the user you want to delete: ")

        worksheet = SHEET.worksheet('Issue')
        user_rows = worksheet.get_all_values()
        user_row = None
        for row in user_rows[1:]:
            if row[0] == user_id:
                user_row = row
                break

        if user_row is None:
            print(f"No user is found with ID {user_id}.") 
            continue

        worksheet.delete_row(user_rows.index(user_row)+1)
        print(f"The User with ID {user_id} has been deleted.")

    elif action == 'quit':
        break

    else: 
        print("Invalid input.Please enter 'search', 'add', 'update' or 'quit'")


user_issues = SHEET.worksheet('Issue')

issues = user_issues.get_all_values()

print("Issue ID:", issue_id_formatted)

print("IT Issue category:", chosen_category)

print("User Issue:", issue_description)

print("User Contact Number:", contact_number)

print("IT Issue Date Created:", issue_date_created)

print(issues)     