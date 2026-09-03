import os
import pandas as pd

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
