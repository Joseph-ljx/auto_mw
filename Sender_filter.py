
def sender_filter():
    filter_list = ['csc', 'Equinix Maintenance', 'RCP.Frankfurt@telekom.de', 'GCX Change Management',
                   'Flexential Support', 'Planned Work/Maintenance <infraco.cm@exainfra.net>',
                   "Digital Realty Customer Portal <customerportal@digitalrealty.com>"]
    # sender_list = ['No-Reply@Lumen.com', 'MR Zayo', 'americas-csc@verizonbusiness.com', 'ncm@arelion.com',
    # 'Cogent-NoReply@cogentco.com']
    sender_list = ['americas-csc@verizonbusiness.com', 'Cogent-NoReply@cogentco.com']
    subject_list = []
    return sender_list, subject_list
