import os
import re
import pandas as pd
from datetime import datetime, date

# Activity 1
FILE_NAME = "Python_Training_Bootcamp_Activity.xlsx"
#create excel function
def create_excel():
    if os.path.exists(FILE_NAME):
        print(f"⇒ An excel file with the name {FILE_NAME} already exists.")
        print("⇒ What would you like to do?")
        print("1. Overwrite the existing file (this will delete all existing data)")
        print("2. Cancel and go back to the main menu")

        while True:
            choice = input("Enter your choice (1 or 2): ").strip()
            if choice == "1":
                print(f"⇒ Overwriting {FILE_NAME}...")
                break
            elif choice == "2":
                print("⇒ Operation cancelled. Returning to the main menu.")
                return False
            else:
                print("⇒ Invalid choice. Please enter 1 or 2.")

    try:
        df = pd.DataFrame(columns=["Name", "Email Address", "Address", "Birthday", "Age"])
        df.to_excel(FILE_NAME, index=False)
        print(f"⇒ {FILE_NAME} created successfully.")
        print(f"⇒ File path: {os.path.abspath(FILE_NAME)}")

        print("\n Would you like to add a new record to the excel file?")
        print("1. Yes add a record")
        print("2. No (Return to main menu)")

        while True:
            choice = input("Enter your choice (1 or 2): ").strip()
            if choice == "1":
                update_excel()
                break
            elif choice == "2":
                print("⇒ Returning to the main menu.")
                break
            else:
                print("⇒ Invalid choice. Please enter 1 or 2.")
        return True
    
    except PermissionError:
        print(f"⇒ Permission denied. Unable to create {FILE_NAME}.")
        return False
    except Exception as e:
        print(f"⇒ An error occurred while creating {FILE_NAME}: {e}")
        return False
    
# Activity 2
#validate date function
def validate_date(date_str):
    if not date_str or not date_str.strip():
        print("⇒ Date cannot be empty.")
        return None
    
    try:
        birthday = datetime.strptime(date_str, "%Y-%m-%d").date()
        if birthday > date.today():
            print("⇒ Birthday cannot be in the future.")
            return None
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

#email validation function
def validate_email(email):
    if not email or not email.strip():
        print("⇒ Email address cannot be empty.")
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

#user input function
def user_input():
    print("\nPlease provide the following information:")
    while True:
        name = input("Enter your name: ").strip()
        if name:
            break
        print("⇒ Name cannot be empty. Please enter your name.")
    
    while True:
        email = input("Enter your email address: ").strip()
        if not email:
            print("⇒ Email address cannot be empty. Please enter your email address.")
        elif validate_email(email):
            break
        else:
            print("⇒ Invalid email format. Please enter a valid email address.")

    while True:
        address = input("Enter your address: ").strip()
        if address == "":
            print("⇒ Address cannot be empty. Please enter your address.")
        else:
            break

    while True:
        birth_date = input("Enter your birthday (YYYY-MM-DD): ").strip()
        birthday = validate_date(birth_date)
        if birthday:
            break

    age = calculate_age(birthday)

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

# Main Menu
def display_menu():
    print("\nWelcome to the Python Training Bootcamp!")
    print("Please choose an option:")
    print("1. Create Excel File")
    print("2. Update Excel File")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            create_excel()
        elif choice == "2":
            update_excel()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("⇒ Invalid choice. Please enter 1, 2, or 3.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()