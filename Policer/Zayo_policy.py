def zayo(message):
    """
    This is the policy for Lumen.
    We need to specify rules and characteristics of email
    """
    body = message.body.splitlines()
    my_time = []
    cid = []
    reason = ""
    duration = ""

    # print(body)
    for content in body:
        if "Reason for Maintenance" in content:
            reason = content

        # Format Time
        if "GMT" in content:
            my_time.append(content)

        # Format CID
        if "//ZYO" in content:
            cur = content.split("\t")
            cid.append(cur[0])

            # Format duration
            duration = cur[1]

    return reason, my_time, cid, duration
