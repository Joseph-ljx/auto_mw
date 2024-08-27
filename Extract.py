from datetime import datetime


def extract_information(message, cid_dict):
    subject = message.Subject
    sender = message.SenderName
    body = message.body.splitlines()
    received_time = message.ReceivedTime
    my_time = []
    reason = ""
    cid = []
    save_email_flag = False
    # Lumen
    if sender == 'No-Reply@Lumen.com':
        # print(body)
        for content in body:
            if "Lumen intend" in content or "Lumen will" in content or "Lumen's 3rd party" in content:
                reason = content
                # print(reason)
            if "Greenwich Mean Time" in content:
                my_time.append(content.replace("\t", ""))
                # print(my_time)
            if ("CHINA TELECOM (AMERICAS) CORPORATION" in content or "CHINA TELECOM AMERICAS" in content
                    or "CHINA TELECOM (USA) CORPORATION" in content):
                cur = content.split("\t")
                cid.append(cur[1].replace(" ", ""))
                # print(cid)
    # if sender == "ZAYO"
    # if sender == "Verizon"
    # if sender == "Arelion"

        # Format the important information
        if cid:
            print("=" * 50)
            print(f"Subject: {subject}")
            print(f"Sender: {sender}")
            print(f"Received Time: {received_time}")
            print(f"Reason for MW: {reason}\nVendor CID is {cid}\nTime is {my_time}")
            print("=" * 50)
            now = datetime.now()
            year, month, day = now.year, now.month, now.day
            filename = f"MW_info_{year}-{month}-{day}"
            with open(filename, 'a') as w:
                for cur_cid in cid:
                    all_info = f"Subject: {subject}\n" + f"Reason for MW: {reason}\nVendor CID is {cur_cid}\nTime is {my_time}\n"
                    if cur_cid in cid_dict:
                        w.write(all_info)
                        w.write(f"CT CID: {cid_dict[cur_cid]}")
                        w.write("\n\n")
                        save_email_flag = True
                    if cur_cid not in cid_dict:
                        w.write(all_info)
                        w.write(f"Customer's CID or not in the database. Check manually!")
                        w.write("\n\n")
    return save_email_flag
