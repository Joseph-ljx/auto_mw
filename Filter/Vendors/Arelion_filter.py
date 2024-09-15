def arelion_filter(subject, sender):

    """
    This is the Arelion filter.

    We decide the email from lumen whether it is a necessary email we need

    * True: This email has something that we do not want, exclude it
    * None: We will consider this email

    """

    if sender == 'ncm@arelion.com':
        if any(word in subject for word in ['Reminder']):
            return True
