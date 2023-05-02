"""
IT Issue Tracking Management System
The script allows users to manage IT Issues
"""

from datetime import datetime

import gspread 
from google.oauth2.service_account import Credentials

import sys

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


# Define search issues function, returning issue information on search criteria  

def search_issues(search_term):
    worksheet = SHEET.worksheet('Issue')
    issues = worksheet.get_all_values()

    results = []
    for issue in issues[1:]:
        for value in issue:
            if search_term.lower() in value.lower():
                results.append(issue)
                break
    
    if results:

        try:
            print(f"Search results for '{search_term}':")

            for issue in results:
                print("\t".join(issue))
             
        except Exception as e:
            print(f"No results found for '{search_term} {e}'.")


chosen_category = ''
issue_description = ''
contact_number = ''
issue_date_created = ''
issue_id_formatted = ''


# Define add issue function and prompt user to add issue related information

def add_issue():

    issue_id_counter = get_max_id() + 1

    print("Welcome to the add user issue action !")

    print("----------")

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

    try:

        print("Issue has been added successfully!")

    except Exception as e:
        print(f"An error occured while adding an issue: {e}")
        exit()


issue_id_formatted = issue_id_formatted
chosen_category = chosen_category
issue_description = issue_description
contact_number = contact_number
issue_date_created = issue_date_created


# Define a function to update the issue sheet
def update_issue():
    
    print('Welcome to SmartITFlow, the IT Issue Tracking Management System!')


worksheet = SHEET.worksheet('Issue')
user_id = input('Enter the User_ID: ')
row_num = None
while not row_num:
    # Find the row number for the given User_ID
    user_ids = worksheet.col_values(1)
    row_num = user_ids.index(user_id) + 1 if user_id in user_ids else None
    if not row_num:
        print(f"No rows found for User_ID '{user_id}'")
        user_id = input('Enter the User_ID: ')
            
    # Ask the user which field they want to edit
field_names = ['Category', 'Issue Description', 'Forename', 'Surname', 
               'Contact Number', 'Priority Level', 'Due_Date', 'Status', 
               'Resolution_Time', 'Resolution_Notes']
field_num = None
while not field_num:
    print("Which field do you want to update?")
    for i, name in enumerate(field_names):
        print(f"{i+1}. {name}")
    choice = input("Enter the number corresponding to the field: ")
    if choice.isdigit() and int(choice) in range(1, len(field_names)+1):
        field_num = int(choice)
    else:
        print("Invalid choice. Please enter a valid number.")
    
    # Ask the user for the new value
    new_value = input(f"Enter the new value for {field_names[field_num-1]}: ")
    
    # Update the appropriate column in the row for the given User_ID
    col_num = field_num + 1  # Column 1 is the User_ID column
    worksheet.update_cell(row_num, col_num, new_value)
    print(f"{field_names[field_num-1]} for User_ID '{user_id}' " 
          f"updated with value '{new_value}'")


def delete_issue():

    print("Welcome to the delete user action!")
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

    worksheet.delete_row(user_rows.index(user_row)+1)
    print(f"The User with ID {user_id} has been deleted.")


def quit():
    print("Exiting SmartITFlow...")
    sys.exit()


while True:

    # Define user input actions adding specified functions

    action = input('Enter action (search / add / update / delete / quit): ')

    if action == 'search':
        search_term = input('Enter search term: ')
        search_issues(search_term)

    elif action == 'add issue':
        add_issue()

    elif action == 'update':
        update_issue()

    elif action == 'delete':
        delete_issue()

    elif action == 'quit':
        quit() 

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