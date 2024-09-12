def verizon_filter(subject, sender):

    """
    This is the Verizon filter.

    We decide the email from lumen whether it is a necessary email we need

    * True: This email has something that we do not want, exclude it
    * None: We will consider this email

    """

    # Verizon sometimes send notification in 3-4 days in advanced marked as 'Emergency'
    if sender == 'americas-csc@verizonbusiness.com':
        if any(word in subject for word in ["REMINDER", "CANCELLED", "COMPLETED"]):
            return True
