# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Accounting New Financial Reports',
    'summary': 'View financial reports',
    'category': 'Accounting/Accounting',
    'description': """
Accounting New Financial Reports
==================
    """,
    'depends': ['account_reports'],
    'data': [
        'data/account_erp_financial_report_data.xml',
    ],
    'qweb': [],
    'auto_install': False,
    'installable': True,
    'license': 'OPL-1',
}
