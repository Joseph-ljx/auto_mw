
def verizon(message):
    body = message.body.splitlines()
    my_time = []
    reason = ""
    cid = []
    print(body)
    for index, content in enumerate(body):
        if any(word in content for word in ["We will be", "A Third Party vendor will be"]):
            reason = content
            print(reason)
        if "Maintenance Date/Time (GMT)" in content and '\t' not in content:
            my_time.append(body[index+2])
            print(my_time)
        if "Maintenance Date/Time (GMT):\t" in content:
            my_time.append(content.split('\t')[1])
            print(my_time)
        if any(word in content for word in ["CHINA TELECOM (USA) CORP.", "CHINA TELECOM USA CORPORATION",
                                            "CHINA TELECOM (AMERICAS) CORPORATION", "CHINA TELECOM CORP"]):
            cur = content.split("\t")
            cid.append(cur[1].replace(" ", ""))
            print(cid)

    return reason, my_time, cid
