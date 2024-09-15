def verizon(message):

    """
    This is the policy for Verizon.
    We need to specify rules and characteristics of email
    * body: The body of the email message
    * my_time: Scheduled maintenance time
    * Vendor's cid: Circuit ID
    * Duration: Maintenance time frame
    """

    # Cut the message in lines
    body = message.body.splitlines()
    my_time = []
    reason = ""
    duration = ""
    cid = []

    # Loop body information:
    for index, content in enumerate(body):
        if any(word in content for word in ["We will be", "A Third Party vendor will be"]):
            reason = content

        # body[index+2] 指的是当前行的两行之后的内容。也就是说，如果当前行是 index，那么 body[index+2] 就是 index+2 位置的内容
        if "Maintenance Date/Time (GMT)" in content and '\t' not in content:
            my_time.append(body[index+2])

        # Maintenance time
        if "Maintenance Date/Time (GMT):\t" in content:
            my_time.append(content.split('\t')[1])

        # Duration
        if "Planned Circuit Downtime" in content and '\t' not in content:
            duration = body[index+2]

        # Circuit to be reported
        if any(word in content for word in ["CHINA TELECOM (USA) CORP.", "CHINA TELECOM USA CORPORATION",
                                            "CHINA TELECOM (AMERICAS) CORPORATION", "CHINA TELECOM CORP"]):
            cur = content.split("\t")
            cid.append(cur[1].replace(" ", ""))

    return reason, my_time, cid, duration
