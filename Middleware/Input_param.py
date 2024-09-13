"""
This Function is used for inputting params for checking the relevant emails in a certain period
* Start Time: start
* End Time: end
* Folder: maintenance folder
* Account Name: email address
"""
import os
from datetime import datetime
import json
from turtledemo.penrose import start


def  input_param():

    # # Set the filter start time
    # start = input("Enter the filter start time like: 2024,8,29,10,2 (No ahead zero like 08)\n")
    # start = start.split(",")
    # start_date = datetime(int(start[0]), int(start[1]), int(start[2]), int(start[3]), int(start[4]))
    # print(f"Your start time: {start_date}")
    #
    # # Set the filter's end time
    # end = input("Enter the filter end time like: 2024,8,29,10,2 (No ahead zero like 08)\n")
    # end = end.split(",")
    # end_date = datetime(int(end[0]), int(end[1]), int(end[2]), int(end[3]), int(end[4]))
    # print(f"Your end time: {end_date}")
    #
    # # Set the folder name (Maintenance folder)
    # folder_name = input("Please enter the folder for you: \n")
    #
    # # Set the account name
    # account_name = input("Please enter your personal CTA email address: \n")
    # return start_date, end_date, folder_name, account_name

    try:
        # Ensure the path as absolute path
        file_path = os.path.abspath('../Database/Params.json')

        # Read JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            # 加载 JSON 数据
            data = json.load(file)

        # Print values
        # print("User:", data.get('user', 'N/A'))
        # print("Start Date:", data.get('date').get('end_Date', 'N/A'))
        # print("End Date:", data.get('date', {}).get('end_Date', 'N/A'))

    # Exception Handling
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Assign and return params information
    user = data.get('user', 'N/A')
    account_name = data.get('account_name', 'N/A')
    folder_name = data.get('folder_name', 'N/A')

    # Format start date
    start = data.get('date', {}).get('start_Date', 'N/A')
    start = start.split(".")
    start_date = datetime(int(start[0]), int(start[1]), int(start[2]), int(start[3]), int(start[4]))

    # Format end date
    end = data.get('date', {}).get('end_Date', 'N/A')
    end = end.split(".")
    end_date = datetime(int(end[0]), int(end[1]), int(end[2]), int(end[3]), int(end[4]))

    return user, account_name, folder_name, start_date, end_date

### TESTING ###
# if __name__ == "__main__":
#     input_param()

# 为什么要加空的 {}:
# 添加空字典 {} 作为 data.get('date', {}) 的默认值
# 确保即使 'date' 键缺失，我们不会在尝试从其值中获取 'start_Date' 键时遇到问题。
# 如果没有这个空字典作为默认值，data.get('date') 在 'date' 键缺失的情况下将返回 None
# 并且尝试在 None 上调用 .get('start_Date') 会导致 AttributeError 异常。
# 使用空字典 {} 避免了这种情况。
