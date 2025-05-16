# -*- coding: utf-8 -*-
{
    'name': "prueba",

    'summary': "Ejercicios",

    'description': """
    Ejercicios
    """,

    'author': "Inigo",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base'],
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'prueba/static/src/js/precio_cero_alerta.js',
            'prueba/static/src/js/cliente_idioma_columna.js',
            #'prueba/static/src/js/boleta_button.js',
            #'prueba/static/src/xml/boleta_button.xml',
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}

