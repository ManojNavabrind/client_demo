# -*- coding: utf-8 -*-
{
    'name': 'Odoo Planogram',
    'category': 'Sales',
    'author': "Navabrind IT Solutions Pvt Ltd",
    'website': "www.navabrindsol.com",
    'version': '16.0',
    'description': "Iframe for planogram",
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/planogram_view.xml',
	],
    'installable': True,
    'application': True,
    'auto_install': False,
}
