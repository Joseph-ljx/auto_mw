from win32com.client import Dispatch
import os
import re
from datetime import datetime

from Middleware.Input_param import input_param
from Middleware.Extract import extract_information
from Middleware.Read_csv import read_csv
from Middleware.Write_textMail import write_textMail
from Filter.Main_filter import main_filter

# Read the needed information from Params
# user: Primary key for distinguish
# account_name: Email address
# folder_name: Folder to enter
# start_date: Start filter time
# end_date: End filter time
user, account_name, folder_name, start_date, end_date = input_param()

now = datetime.now()
year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute

# Connect to the local cache outlook
outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
filtered_messages = []

# Backbone database, read from CSV (Data load only need one time)
cid_dict = read_csv()

"""
This is the Main function for this script

"""

# Filter email base on the start time and end time
# We need to find out the emails in a specific time range
for account in outlook.Folders:
    print(f"Account: {account.Name}")

    # Could find this account, accumulate the email messages
    if account.Name == account_name:

        # Microsoft Outlook Object
        # Enter top folder "Inbox":
        Inbox = account.Folders["Inbox"]

        # Enter sub-folder:
        Maintenance = Inbox.folders[folder_name]
        print(f"Searching in Folder: {Maintenance.Name}")

        # Extract all emails
        messages = Maintenance.items
        messages.Sort("[ReceivedTime]", True)

        for message in messages:
            if message.Class == 43:
                received_time = message.ReceivedTime
                received_time_naive = received_time.replace(tzinfo=None)
                if start_date <= received_time_naive <= end_date:

                    # Concluded messages into filtered messages
                    filtered_messages.append(message)
        break

# Loop through each message that in the time range
# We need to figure out all the message that live up to our expectation
for message in filtered_messages:
    subject = message.Subject
    sender = message.SenderName
    received_time = message.ReceivedTime
    body = message.body

    # Enter the filters
    # Exclude useless emails
    if main_filter(subject, sender):
        continue

    # Extract relevant information
    # Determine  whether it is a backbone to report on Zong Diao
    backbone = extract_information(message, cid_dict)

    # For Backbone circuit:
    # Save the email as txt
    # Export the email for uploading and prove
    if backbone:
        write_textMail(body, subject)
