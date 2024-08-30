def lumen(message):
    """
    This is the policy for Lumen.
    We need to specify rules and characteristics of email
    """
    body = message.body.splitlines()
    my_time = []
    reason = ""
    cid = []

    # Extract email information
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

    return reason, my_time, cid
