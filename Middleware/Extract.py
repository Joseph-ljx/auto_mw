from datetime import datetime
from Policer.Arelion_policy import arelion
from Policer.Lumen_policy import lumen
from Policer.Zayo_policy import zayo
from Policer.Verizon_policy import verizon

"""
This method is to extract the desired information from each email message
"""
def extract_information(message, cid_dict):
    subject = message.Subject
    sender = message.SenderName
    # print(sender)
    body = message.body.splitlines()
    received_time = message.ReceivedTime

    save_email_flag = False
    my_time = []
    cid = []
    reason = ""
    duration = ""

    # Extract information from different vendors
    if sender == 'No-Reply@Lumen.com':
        reason, my_time, cid, duration = lumen(message)
    elif sender == 'MR Zayo':
        reason, my_time, cid, duration = zayo(message)
    elif sender == "americas-csc@verizonbusiness.com":
        reason, my_time, cid, duration = verizon(message)
    elif sender == "ncm@arelion.com":
        reason, my_time, cid, duration = arelion(message)

    # If CID is not empty (we can identify this circuit)
    if cid:
        print("=" * 50)
        print(f"Subject: {subject}")
        # print(f"Sender: {sender}")
        # print(f"Received Time: {received_time}")
        # print(f"Reason for MW: {reason}\n Vendor CID is {cid}\n Time is {my_time}")
        # print("=" * 50)
        now = datetime.now()
        year, month, day = now.year, now.month, now.day
        filename = f"MW_info_{year}-{month}-{day}.txt"

        # Open a file and write the conclusion for Circuit to report
        with (open(filename, 'a') as w):

            # Loop all the circuit need maintenance:
            for cur_cid in cid:
                all_info = f"Subject: {subject}\n" + f"Reason for MW: {reason}\n Vendor CID: {cur_cid}\n Time: {my_time}\n Duration: {duration}\n"

                # Backbone Circuit
                if cur_cid in cid_dict:
                    w.write(all_info)
                    w.write(f"CT CID: {cid_dict[cur_cid]}")
                    w.write("\n\n")
                    save_email_flag = True

                # Customer Circuit | Unknown
                if cur_cid not in cid_dict:
                    w.write(all_info)
                    w.write(f"Customer's CID or not in the database. Check manually!")
                    w.write("\n\n")

    return save_email_flag
