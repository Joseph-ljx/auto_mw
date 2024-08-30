def zayo(message):
    """
    This is the policy for Lumen.
    We need to specify rules and characteristics of email
    """
    body = message.body.splitlines()
    my_time = []
    reason = ""
    cid = []
    # print(body)
    for content in body:
        if "Reason for Maintenance" in content:
            reason = content
            print(reason)
        if "GMT" in content:
            my_time.append(content)
            print(my_time)
        if "//ZYO" in content:
            cur = content.split("\t")
            cid.append(cur[0])
            print(cid)

    return reason, my_time, cid
