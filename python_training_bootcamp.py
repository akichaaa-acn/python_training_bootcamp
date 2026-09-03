import os
import pandas as pd

# Activity 1
FILE_NAME = "python_training_bootcamp.xlsx"
#create excel function
def create_excel():
    try:
        df = pd.DataFrame(columns=["Name", "Email Address", "Address", "Birthday", "Phone Number"])

        df.to_excel(FILE_NAME, index=False)
        print(f"⇒ {FILE_NAME} created successfully.")
        return True

    except PermissionError:
        print(f"⇒ Permission denied: Unable to create {FILE_NAME}. Please check your file permissions.")
        return False
    except Exception as e:
        print(f"⇒ An error occurred while creating {FILE_NAME}: {e}")
        return False

