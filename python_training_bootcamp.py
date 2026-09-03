import os
import pandas as pd
from datetime import datetime, date

# Activity 1
FILE_NAME = "python_training_bootcamp.xlsx"
#create excel function
def create_excel():
    try:
        df = pd.DataFrame(columns=["Name", "Email Address", "Address", "Birthday", "Age"])
        df.to_excel(FILE_NAME, index=False)
        print(f"⇒ {FILE_NAME} created successfully.")
        print(f"⇒ File path: {os.path.abspath(FILE_NAME)}")
        return True

    except PermissionError:
        print(f"⇒ Permission denied: Unable to create {FILE_NAME}. Please check your file permissions.")
        return False
    except Exception as e:
        print(f"⇒ An error occurred while creating {FILE_NAME}: {e}")
        return False

# Activity 2
#validate date function
def validate_date(date_str):
    try:
        birthday = datetime.strptime(date_str, "%Y-%m-%d").date()
        if birthday > date.today():
            print("⇒ Birthday cannot be in the future.")
            return None
        else:
            return birthday
    except ValueError:
        print("⇒ Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return None

#calculate age function
def calculate_age(birthday):
    today = date.today()
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    return age

#user input function
def user_input():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    address = input("Enter your address: ")
    birthday = input("Enter your birthday (YYYY-MM-DD): ")
    age = input("Enter your age: ")

    return {
        "Name": name,
        "Email Address": email,
        "Address": address,
        "Birthday": birthday,
        "Age": age
    }

#update excel function
def update_excel():
    if not os.path.exists(FILE_NAME):
        print(f"⇒ {FILE_NAME} does not exist. Please create the file first.")
        return False

    user_data = user_input()

    try:
        df = pd.read_excel(FILE_NAME)

        new_row = pd.DataFrame({
            "Name": [user_data["Name"]],
            "Email Address": [user_data["Email Address"]],
            "Address": [user_data["Address"]],
            "Birthday": [user_data["Birthday"]],
            "Age": [user_data["Age"]]
        })

        df = pd.concat([df, new_row], ignore_index=True)

        df.to_excel(FILE_NAME, index=False)
        print(f"⇒ {FILE_NAME} updated successfully.")
        print(f"⇒ Name: {user_data['Name']}\n⇒ Email Address: {user_data['Email Address']}\n⇒ Address: {user_data['Address']}\n⇒ Birthday: {user_data['Birthday']}\n⇒ Age: {user_data['Age']}")
        return True
    except PermissionError:
        print(f"⇒ Permission denied: Unable to update {FILE_NAME}. Please check your file permissions.")
        return False
    except Exception as e:
        print(f"⇒ An error occurred while updating {FILE_NAME}: {e}")
        return False
    