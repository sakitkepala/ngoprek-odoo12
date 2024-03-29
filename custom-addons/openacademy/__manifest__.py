# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Tata kelola training""",

    'description': """
        Modul Open Academy untuk tata kelola training:
            - kelas-kelas training
            - sesi-sesi training
            - registrasi peserta
    """,

    'author': "Andika",
    'website': "https://sakitkepala.github.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'views/reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
