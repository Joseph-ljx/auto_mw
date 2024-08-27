from win32com.client import Dispatch
import os
import re
from datetime import datetime
from Sender_filter import sender_filter
from Extract import extract_information
from read_csv import read_csv

# Set the filter start time and end time
start_date = datetime(2024, 8, 23, 11, 0)  # Start date (YYYY, MM, DD)
end_date = datetime(2024, 8, 26, 11, 20)
folder_name = "MW"

outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
filtered_messages = []

for account in outlook.Folders:
    print(f"Account: {account.Name}")
    if account.Name == 'yuxiwang@ctamericas.com':

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
    # print(f"Subject: {subject}")
    # Skip some email
    if subject in subject_list:
        continue
    if "China Telecom (Europe) Limited" in subject and sender == 'nmc':
        continue
    if "Postponed" in subject:
        continue
    if "Cancelled" in subject:
        continue
    if sender not in sender_list:
        continue

    cid_dict = read_csv()
    backbone = extract_information(message, cid_dict)
    if backbone:
        cleaned_text = re.sub(r'[^\w\s]', ' ', subject)
        filename = cleaned_text + '.txt'
        # Write email details to the file
        with open(filename, 'w', encoding='utf-8') as file:
            # file.write(f"Subject: {subject}\n")
            # file.write(f"Sender: {sender}\n")
            # file.write("\n--- Email Body ---\n\n")
            file.write(body)
        print(f"Email saved to {filename}")

