from win32com.client import Dispatch
import os
import re
from datetime import datetime

from Middleware.Input_param import input_param
from Filter.Sender_filter import sender_filter
from Middleware.Extract import extract_information
from Middleware.Read_csv import read_csv
from Middleware.Write_textMail import write_textMail

# Read the needed information from Params
# user: Primary key for distinguish
# account_name: Email address
# folder_name: Folder to enter
# start_date: Start filter time
# end_date: End filter time
user, account_name, folder_name, start_date, end_date = input_param()

now = datetime.now()
year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute

# Read the list information
sender_list, subject_list = sender_filter()

# Connect to the local cache outlook
outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
filtered_messages = []

# Backbone database, read from CSV (Data load only need one time)
cid_dict = read_csv()

"""
This is the Main function for this script

"""

# Filter email base on the start time and end time
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
                # print(received_time)
                received_time_naive = received_time.replace(tzinfo=None)
                if start_date <= received_time_naive <= end_date:
                    # Concluded messages
                    filtered_messages.append(message)
        break

# Judge each message
for message in filtered_messages:
    subject = message.Subject
    sender = message.SenderName
    received_time = message.ReceivedTime
    body = message.body

    # Use "continue" to skip some unmatch email
    # General Skipping using subject
    if subject in subject_list:
        continue

    # Omit CTU & NMC useless email information
    if "China Telecom (Europe) Limited" in subject and sender == 'nmc':
        continue

    # Lumen
    if (any(word in subject for word in ["Postponed", "Cancelled", "Work Ended", "Work Started"])
            and sender == 'No-Reply@Lumen.com'):
        continue

    # Zayo
    if (any(word in subject for word in ["COMPLETED", "UPDATE", "Update", "Verification", "START"])
            and sender == 'MR Zayo'):
        continue

    # Verizon
    if ((any(word in subject for word in ["REMINDER", "CANCELLED", "COMPLETED"]))
            and sender == 'americas-csc@verizonbusiness.com'):
        continue

    # Unrecognized sender
    if sender not in sender_list:
        continue

    # Judge whether (each message) it is a backbone to report on Zong Diao
    backbone = extract_information(message, cid_dict)

    # Backbone circuit, save the email as txt, export the email for uploading and prove
    if backbone:
        write_textMail(body, subject)
