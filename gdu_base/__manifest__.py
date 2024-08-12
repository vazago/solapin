# -*- coding: utf-8 -*-
{
    'name': "gdu_base",

    'summary': """
        Gestionar información base para el desarrollo de las aplicaciones de la Universidad de Oriente
    """,

    'description': """
        Gestionar información base para el desarrollo de las aplicaciones de la Universidad de Oriente
    """,

    'author': "DINF-DevGroup",
    'website': "https://www.gdu.uo.edu.cu",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'gdu_users'],
	'application': True,

    # always loaded
    'data': [
        'data/gdu_base_area_data.xml',
        'data/gdu_base_departamento_data.xml',

        'security/ir.model.access.csv',

        'views/gdu_base_departamento_views.xml',
        'views/gdu_base_area_views.xml',
        'views/gdu_base_importaciones_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}