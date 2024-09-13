def lumen_filter(subject, sender):

    """
    This is the Lumen filter.

    We decide the email from lumen whether it is a necessary email we need

    * True: This email has something that we do not want, exclude it
    * None: We will consider this email

    """

    if sender == 'No-Reply@Lumen.com':
        if any(word in subject for word in ["Postponed", "Cancelled", "Work Ended", "Work Started", "Progress Update"]):
            return True