"""
This Function is used for inputting params for checking the relevant emails in a certain period
* Start Time: start
* End Time: end
* Folder: maintenance folder
* Account Name: email address
"""

from datetime import datetime

def  input_param():

    # Set the filter start time
    start = input("Enter the filter start time like: 2024,8,29,10,2 (No ahead zero like 08)\n")
    start = start.split(",")
    start_date = datetime(int(start[0]), int(start[1]), int(start[2]), int(start[3]), int(start[4]))
    print(f"Your start time: {start_date}")

    # Set the filter's end time
    end = input("Enter the filter end time like: 2024,8,29,10,2 (No ahead zero like 08)\n")
    end = end.split(",")
    end_date = datetime(int(end[0]), int(end[1]), int(end[2]), int(end[3]), int(end[4]))
    print(f"Your end time: {end_date}")

    # Set the folder name (Maintenance folder)
    folder_name = input("Please enter the folder for you: \n")

    # Set the account name
    account_name = input("Please enter your personal CTA email address: \n")
    return start_date, end_date, folder_name, account_name


### TESTING ###
# if __name__ == "__main__":
#     input_param = input_param()
