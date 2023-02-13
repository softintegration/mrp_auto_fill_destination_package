# -*- coding: utf-8 -*- 


{
    'name': 'Auto fill destination package from source package in manufacturing',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1',
    'category': 'Manufacturing/Manufacturing',
    'demo': [],
    'depends': ['mrp','product_management_by_package'],
    'data': [
        'views/stock_move_views.xml',
        'views/mrp_production_views.xml'
    ],
    'license': 'LGPL-3',
}
