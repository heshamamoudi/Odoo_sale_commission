# -*- coding: utf-8 -*-
{
    'name': "sales_commission",

    'summary': """
        This Module helps in Automating Sales Commissions and invoiceing it.""",

    'description': """
        This Module helps in Automating Sales Commissions and invoiceing it using on confirming order / invoice 
        / invoice registering payment
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account', 'sale_management', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/Sales_Settings_Sales_commission.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
