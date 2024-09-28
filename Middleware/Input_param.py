"""
This Function is used for inputting params for checking the relevant emails in a certain period
* Start Time: start
* End Time: end
* Folder: maintenance folder
* Account Name: email address
* user: Primary key for distinguish
* account_name: Email address
* folder_name: Folder to enter
* start_date: Start filter time
* end_date: End filter time
* server: Sever
* primary_smtp_address:Primary smtp address
* username: User's email name
* password: password
# recipients = recipients
"""
import os
from datetime import datetime
import json
from turtledemo.penrose import start

def input_param():

    try:
        # Ensure the path as absolute path
        file_path = os.path.abspath('../Database/Params.json')

        # Read JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            # 加载 JSON 数据
            data = json.load(file)

    # Exception Handling
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Assign and return params information
    user = data.get('user', 'N/A')

    # Account Name
    account_name = data.get('account_name', 'N/A')

    # Folder
    folder_name = data.get('folder_name', 'N/A')

    # Format start date
    start = data.get('date', {}).get('start_Date', 'N/A')
    start = start.split(".")
    start_date = datetime(int(start[0]), int(start[1]), int(start[2]), int(start[3]), int(start[4]))

    # Format end date
    end = data.get('date', {}).get('end_Date', 'N/A')
    end = end.split(".")
    end_date = datetime(int(end[0]), int(end[1]), int(end[2]), int(end[3]), int(end[4]))

    # Email Account Information
    server = data.get('email', {}).get('server', 'N/A')
    primary_smtp_address = data.get('email', {}).get('primary_smtp_address', 'N/A')
    username = data.get('email', {}).get('username', 'N/A')
    password = data.get('email', {}).get('password', 'N/A')
    recipients = data.get('email', {}).get('recipients', 'N/A')

    return user, account_name, folder_name, start_date, end_date, server, primary_smtp_address, username, password, recipients

### TESTING ###
# if __name__ == "__main__":
#     input_param()

# 为什么要加空的 {}:
# 添加空字典 {} 作为 data.get('date', {}) 的默认值
# 确保即使 'date' 键缺失，我们不会在尝试从其值中获取 'start_Date' 键时遇到问题。
# 如果没有这个空字典作为默认值，data.get('date') 在 'date' 键缺失的情况下将返回 None
# 并且尝试在 None 上调用 .get('start_Date') 会导致 AttributeError 异常。
# 使用空字典 {} 避免了这种情况。
