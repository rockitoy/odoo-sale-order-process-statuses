# -*- coding: utf-8 -*-
# Copyright (C) 2019-present  Technaureus Info Solutions(<http://www.technaureus.com/>).

{
    'name': 'Odoo Sales Order Process Status',
    'version': '12.0.0.0',
    'category': 'Sales',
    'summary': 'Process status',
    'sequence': 1,
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'website': 'http://www.technaureus.com/',
    'description': """
    """,
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/process_status_view.xml',
        'views/sale_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
