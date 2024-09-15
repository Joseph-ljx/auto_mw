def lumen(message):
    """
    This is the policy for Lumen.
    We need to specify rules and characteristics of email
    * body: The body of the email message
    * my_time: Scheduled maintenance time
    * Vendor's cid: Circuit ID
    * Duration: Maintenance time frame
    """
    body = message.body.splitlines()
    my_time = []
    cid = []
    reason = ""
    duration = ""

    # Extract email information
    for content in body:
        if "Lumen intend" in content or "Lumen will" in content or "Lumen's 3rd party" in content:
            reason = content

        # Time
        if "Greenwich Mean Time" in content:
            my_time.append(content.replace("\t", ""))
            # print(my_time)

        # CTA report circuit
        if ("CHINA TELECOM (AMERICAS) CORPORATION" in content or "CHINA TELECOM AMERICAS" in content
                or "CHINA TELECOM (USA) CORPORATION" in content):
            cur = content.split("\t")
            cid.append(cur[1].replace(" ", ""))

            # Extract time duration information
            duration = cur[7]

    return reason, my_time, cid, duration
