{
    'name': 'Journal Dashboard Balance from General Ledger',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': "Show a journal's true GL balance on the dashboard card when its Outstanding accounts are set to its own default account",
    'description': """
        For a bank/cash journal where the Outstanding Receipts/Payments account
        is set to the journal's own default account, Odoo's dashboard "Balance"
        card (last statement balance + transactions since) only ever grows: every
        payment posted through the journal is immediately flagged as matched, and
        the offsetting clearing entry created when a bank statement line is later
        reconciled against that payment is invisible to that calculation. For
        journals configured this way, this module shows the account's real
        General Ledger balance instead.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['account_accountant'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
