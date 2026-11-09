# -*- coding: utf-8 -*-
{
    'name': 'KVS Customer Statement',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Prints the company stamp and payment details at the bottom of the Customer Statement PDF',
    'description': """
KVS Customer Statement
======================
Customises the printed (PDF) Customer Statement from Accounting:

* A "Company Stamp" image field on the company (Settings > Companies),
  printed at the bottom of the statement.
* The company's Default Terms & Conditions (Accounting Settings > Customer
  Invoices > Default Terms & Conditions) - the same payment details that
  pre-fill every invoice - printed at the bottom of the statement as-is.

Only the Customer Statement is changed. The Follow-up report shares the same
PDF template but is left as it is.
    """,
    'author': 'GlobX',
    'website': 'https://www.theglobx.com',
    'license': 'LGPL-3',
    'depends': [
        'account_reports',
    ],
    'data': [
        'views/res_company_views.xml',
        'report/customer_statement_pdf_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
