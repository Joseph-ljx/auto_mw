from exchangelib import Credentials, Account, Message, Configuration, FileAttachment
from exchangelib import DELEGATE
from datetime import datetime
import os

"""
Send the email to personal's email for confirmation
* This method could connect to the personal's outlook exchange account
* This will send an confirmation letter to account for reference information
*
"""
def send_exchange_mail(server, primary_smtp_address, username, password, recipients):

    # Obtain current date time information
    now = datetime.now()
    year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute

    # Generate Email

    # Step 1: Configurate connection
    credentials = Credentials(username = primary_smtp_address, password = password)
    config = Configuration(server = server, credentials = credentials)

    # Step 2: Connect to your account
    account = Account(primary_smtp_address = primary_smtp_address, credentials = credentials, autodiscover = False,
                      access_type = DELEGATE, config = config)

    # Step 3: Create and send the email
    message = Message(
        account = account,
        folder = account.sent,  # set the sent folder to store a copy of the sent email
        subject = f'Automation report for {month} {day}, {year}. Ending on {hour}:{minute}',
        body = 'Please refer to the attached documents for reporting maintenance and viewing the necessary information!',
        to_recipients = recipients  # List of recipients
    )

    # Step 4: Attach maintenance information .txt
    info_path = f"../Output/MW_info_{year}-{month}-{day}.txt"
    with open(info_path, 'rb') as f:
        content = f.read()
        attachment = FileAttachment(name = f"MW_info_{year}-{month}-{day}.txt", content = content)
        message.attach(attachment)

    # Step 4': Attach all vendor's email in .txt format files
    vendor_email_path = f"../Output/Email_Dir_{year}-{month}-{day}"
    for file_name in os.listdir(vendor_email_path):
        if file_name.endswith('.txt'):  # Only attach .txt files
            file_path = os.path.join(vendor_email_path, file_name)
            with open(file_path, 'rb') as f:
                content = f.read()
                attachment = FileAttachment(name = file_name, content = content)
                message.attach(attachment)


    # Step 5: Send and save the message
    print("=" * 50)
    message.send_and_save()
    print("Email sent successfully with all .txt files attached!")
