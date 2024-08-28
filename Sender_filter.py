
def sender_filter():
    filter_list = ['csc', 'Equinix Maintenance', 'RCP.Frankfurt@telekom.de', 'GCX Change Management',
                   'Flexential Support', 'Planned Work/Maintenance <infraco.cm@exainfra.net>',
                   "Digital Realty Customer Portal <customerportal@digitalrealty.com>"]
    sender_list = ['No-Reply@Lumen.com', 'MR Zayo']
    subject_list = []
    return sender_list, subject_list
