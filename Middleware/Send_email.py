from exchangelib import Credentials, Account, Message, Configuration
from exchangelib import DELEGATE
from datetime import datetime

# Os will always work in the /root dir, make sure it import correctly
from Middleware.Input_param import input_param

# Obtain current date time information
now = datetime.now()
year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute

"""
Send the email to personal's email for confirmation
* This method could connect to the personal's outlook exchange account
* This will send an confirmation letter to account for reference information
*
"""
def send_exchange_mail(server, primary_smtp_address, username, password, recipients):

    # Step 1: Configurate connection information
    credentials = Credentials(username = primary_smtp_address, password = password)
    config = Configuration(server = server, credentials = credentials)

    # Step 2: Connect to your account
    account = Account(primary_smtp_address = primary_smtp_address, credentials = credentials, autodiscover = False,
                      access_type = DELEGATE, config = config)

    # Step 3: Create and send the email
    message = Message(
        account = account,
        folder = account.sent,  # set the sent folder to store a copy of the sent email
        subject = f'Automation report for {month} {day}, {year}: {hour} - {minute}',
        body = 'Please refer to the attached documents for reporting maintenance and viewing the necessary information!',
        to_recipients = recipients  # List of recipients
    )

    # Step 4: Send and save the message
    message.send_and_save()
    print("Email sent successfully!")
