# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Management',
    'version': '14.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoo-teste-hospital.com',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/pacient.xml',
        'views/sale.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
