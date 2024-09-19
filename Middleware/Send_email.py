from exchangelib import Credentials, Account, Message, Configuration
from exchangelib import DELEGATE
import pandas as pd

# Step 1: Get the account
account_db = pd.read_json('../Database/email_account.json')
account = account_db.to_dict(orient='records')[0]
print(account)
credentials = Credentials(username=account['primary_smtp_address'], password=account['password'])
config = Configuration(server=account['server'], credentials=credentials)

# Step 2: Connect to your account
account = Account(primary_smtp_address=account['primary_smtp_address'], credentials=credentials, autodiscover=False,
                  access_type=DELEGATE, config=config)

# Step 3: Create and send the email
message = Message(
    account=account,
    folder=account.sent,  # Sent folder to store a copy of the sent email
    subject='Test email from exchangelib',
    body='This is a test email sent for auto MW.',
    to_recipients=['yuxiwang@ctamericas.com']  # List of recipients
)

# Step 4: Send and save the message
message.send_and_save()
print("Email sent successfully!")
