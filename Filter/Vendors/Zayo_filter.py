def zayo_filter(subject, sender):

    """
    This is the ZAYO filter.

    We decide the email from lumen whether it is a necessary email we need

    * True: This email has something that we do not want, exclude it
    * None: We will consider this email

    """

    if sender == 'MR Zayo':
        if any(word in subject for word in ["COMPLETED", "UPDATE", "Update", "Verification", "START"]):
            return True
