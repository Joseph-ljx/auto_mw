from textfsm import TextFSM
from datetime import datetime
from win32com.client import Dispatch

def arelion(message):
    """
    This is the policy for Arelion.
    We need to specify rules and characteristics of email
    * body: The body of the email message
    * my_time: Scheduled maintenance time
    * Vendor's cid: Circuit ID
    * Duration: Maintenance time frame
    """
    body = message.body
    my_time = []
    reason = ""
    cid = []

    with open('Plugin/Arelion.textfsm', encoding='utf8') as textfsm_file:
        template = TextFSM(textfsm_file)
        datas = template.ParseTextToDicts(body)
        status = []
        for line in datas:
            # print(line)
            if len(line['WORK_STATUS']) != 0:
                status.append(line['WORK_STATUS'])
            if len(line['REASON']) != 0:
                reason = line['REASON']
            if len(line['WINDOW_START']) != 0 and status.pop(0) == "Confirmed":
                temp = line['WINDOW_START'] + ' ' + line['WINDOW_END']
                my_time.append(temp)
                if len(line['IMPACT_SERVICE_ID']) != 0:
                    # print(line['IMPACT_SERVICE_ID'])
                    cid.append(line['IMPACT_SERVICE_ID'])
            # if any(word in line['UPDATE_CONTENT'] for word in ["rescheduled", "Implemented", "Cancelled"]):
            #     return [], "", []

    return reason, my_time, cid


if __name__ == "__main__":
    start_date = datetime(2024, 8, 5, 1, 0)
    end_date = datetime(2024, 8, 5, 1, 2)
    folder_name = ""
    account_name = "ruijiezhu@ctamericas.com"
    ###############################################################################

    now = datetime.now()
    year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute

    # Read the outlook
    outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
    filtered_messages = []

    # List all accounts configured in Outlook
    accounts = outlook.Folders

    # Loop through the accounts to find the one you want
    for account in accounts:
        print(f"Account: {account.Name}")

    target_account = accounts['ruijiezhu@ctamericas.com']

    # Navigate to the Inbox of the specific account
    inbox = target_account.Folders['Inbox']
    Maintenance = inbox.Folders['Maintenance']
    messages = Maintenance.items

    # Convert dates to the format required by Outlook ([mm/dd/yyyy hh:mm AM/PM])
    start_date_str = start_date.strftime("%m/%d/%Y %I:%M %p")
    end_date_str = end_date.strftime("%m/%d/%Y %I:%M %p")

    # Create a filter string
    filter_str = f"[ReceivedTime] >= '{start_date_str}' AND [ReceivedTime] <= '{end_date_str}'"

    # Use the Restrict method to filter the items
    filtered_items = Maintenance.Items.Restrict(filter_str)

    for message in filtered_items:
        reason, my_time, cid = arelion(message)
        print(reason)
        print(my_time)
        print(cid)
        # show_text = message.body
        # print(message.subject)
    pass