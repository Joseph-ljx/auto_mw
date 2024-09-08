def sender_filter():

    """
    This is the filter for different senders.

    We need to make sure that all of the sender are known and deal with their mails with purposes

    """

    redundant_entity_list = ['csc', 'Equinix Maintenance', 'RCP.Frankfurt@telekom.de', 'GCX Change Management',
                   'Flexential Support', 'Planned Work/Maintenance <infraco.cm@exainfra.net>',
                   "Digital Realty Customer Portal <customerportal@digitalrealty.com>"]

    # Known vendors' list
    relevant_entity_list = ['No-Reply@Lumen.com', 'MR Zayo', 'americas-csc@verizonbusiness.com','ncm@arelion.com']

    # Exclude those irrelevant entities
    irrelevant_entity_list = ['nmc']

    return relevant_entity_list, irrelevant_entity_list