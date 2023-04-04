"""
IT Issue Tracking Management System

The script allows users to manage IT Issues
"""

issue_id_counter = 1

issue_description = input("Enter issue description: ")

while True:
    contact_number = input("Enter contact number: ")
    if contact_number.isdigit():
        break
    print("Invalid input. Please enter a number.")

issue_id_formatted = str(issue_id_counter).zfill(2)

if len(issue_id_formatted) == 3:
    issue_id_prefixed = '00' + issue_id_formatted
elif len(issue_id_formatted) == 2:
    issue_id_prefixed = '0' + issue_id_formatted
else:
    issue_id_prefixed = issue_id_formatted


categories = ["Hardware", "Software", "Network", "Other"]
print("IT Issue Category: ")
for i, category in enumerate(categories):
    print(f"{i+1}. {category}")

category_choice = input("Enter the number for the category for the issue: ")
while not category_choice.isdigit() or int(category_choice) < 1 or int(
     category_choice) > len(categories):
    category_choice = input("Invalid input. Enter the category number: ")

chosen_category = categories[int(category_choice)-1]

print("Issue ID:", issue_id_prefixed)

print("IT Issue category:", chosen_category)

print("User Issue:", issue_description)

print("User Contact Number:", contact_number)
