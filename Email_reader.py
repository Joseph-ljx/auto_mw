from win32com.client import Dispatch
import os
import re
from datetime import datetime

from Input_param import input_param
from Sender_filter import sender_filter
from Extract import extract_information
from read_csv import read_csv, read_json

# Set the filter start time, end time, folder_name, account_name
start_date, end_date, folder_name, account_name = input_param()

##############################################################################
# # For test
# start_date = datetime(2024, 8, 6, 2, 30)
# end_date = datetime(2024, 8, 6, 3, 0)
# folder_name = "MW"
# account_name = "yuxiwang@ctamericas.com"
###############################################################################

now = datetime.now()
year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute

# Read the outlook
outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
filtered_messages = []

# Filter email base on the start time and end time
for account in outlook.Folders:
    print(f"Account: {account.Name}")
    if account.Name == account_name:

        inbox = account.Folders[folder_name]
        print(f"Folder: {inbox.Name}")
        messages = inbox.items
        messages.Sort("[ReceivedTime]", True)
        for message in messages:
            if message.Class == 43:
                received_time = message.ReceivedTime
                # print(received_time)
                received_time_naive = received_time.replace(tzinfo=None)
                if start_date <= received_time_naive <= end_date:
                    filtered_messages.append(message)
        break

sender_list, subject_list = sender_filter()
for message in filtered_messages:
    subject = message.Subject
    sender = message.SenderName
    received_time = message.ReceivedTime
    body = message.body
    # print(sender)
    # print(f"Subject: {subject}")

    # Skip some email
    if subject in subject_list:
        continue
    if "China Telecom (Europe) Limited" in subject and sender == 'nmc':
        continue
    # Lumen related
    if (any(word in subject for word in ["Postponed", "Cancelled", "Work Ended", "Work Started"])
            and sender == 'No-Reply@Lumen.com'):
        continue
    # ZAYO related
    if (any(word in subject for word in ["COMPLETED", "UPDATE", "Update", "Verification", "START"])
            and sender == 'MR Zayo'):
        continue
    # Verizon related
    if ((any(word in subject for word in ["REMINDER", "CANCELLED", "COMPLETED"]))
            and sender == 'americas-csc@verizonbusiness.com'):
        continue
    # Arelion related
    if any(word in subject for word in ["Reminder"]) and sender == 'ncm@arelion.com':
        continue
    if sender not in sender_list:
        continue

    # CTA backbone database
    # cid_dict = read_csv()
    cid_dict = read_json()
    # Extract information
    backbone = extract_information(message, cid_dict)

    # Backbone circuit, save the email as txt
    if backbone:
        cleaned_text = re.sub(r'[^\w\s]', ' ', subject)
        filename = cleaned_text + '.txt'
        filename = filename.replace("  ", " ")
        # Create dir
        dir_name = f"Email_Dir_{year}-{month}-{day}"
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        file_path = '\\'.join((dir_name, filename))
        # Write email details to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            # file.write(f"Subject: {subject}\n")
            # file.write(f"Sender: {sender}\n")
            # file.write("\n--- Email Body ---\n\n")
            file.write(body)
        print(f"Email saved to {filename}")
