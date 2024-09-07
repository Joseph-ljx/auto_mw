"""
This is the policy for Verizon.

"""
def sender_filter():
    filter_list = ['csc', 'Equinix Maintenance', 'RCP.Frankfurt@telekom.de', 'GCX Change Management',
                   'Flexential Support', 'Planned Work/Maintenance <infraco.cm@exainfra.net>',
                   "Digital Realty Customer Portal <customerportal@digitalrealty.com>"]

    # Known vendors' list
    sender_list = ['No-Reply@Lumen.com', 'MR Zayo', 'americas-csc@verizonbusiness.com', 'ncm@arelion.com']

    # Subject list is used for excluding mails with specific subject words
    subject_list = []

    return sender_list, subject_list