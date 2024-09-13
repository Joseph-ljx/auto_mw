# Python import always work in the root/ directory
from Filter.General.Sender_filter import sender_filter
from Filter.General.Subject_filter import subject_filter

# Vendors' filters
from Filter.Vendors.Lumen_filter import lumen_filter
from Filter.Vendors.Zayo_filter import zayo_filter
from Filter.Vendors.Arelion_filter import arelion_filter
from Filter.Vendors.Verizon_filter import verizon_filter

# Read the sender list information
relevant_entity_list, irrelevant_entity_list = sender_filter()
subject_list = subject_filter()


def main_filter(subject, sender):

    """
    This is the main filter.

    We decide the email in first general purpose (e.g. nmc? needed? 。。。。)

    Then put into different vendor's detail filter

    * True: This email has something that we do not want, exclude it
    * None: We will consider this email

    """

    ### General filters ###

    # General Skipping using subject keywords
    if subject in subject_list:
        return True

    # We need to exclude those irrelevant senders we already know
    if sender in irrelevant_entity_list:
        return True

    # Should only consider those senders that we know, exclude unknown vendors
    if sender not in relevant_entity_list:
        return True

    ### Vendor's filters ###

    # Lumen filter
    if lumen_filter(subject, sender):
        return True

    # Zayo filter
    if zayo_filter(subject, sender):
        return True

    # Arelion filter
    if arelion_filter(subject, sender):
        return True

    # Verizon filter
    if verizon_filter(subject, sender):
        return True