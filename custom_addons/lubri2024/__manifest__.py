# -*- coding: utf-8 -*-
{
    'name': "lubri2024",

    'summary': """
        Modulos para a empresa Lubrimaster
        """,

    'description': """
        Instala vários módulos designados para o funcionamento da empresa!!!
    """,

    'author': "Yuri Becker",
    'website': "https://www.yuribecker.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale_management',
        'stock',
        'purchase',
        'knowledge',
        'hr_expense',
        'project',
        'website_sale',
        'planning',
        'fleet',
        'contacts',
        'note',
        'calendar',
        'maintenance',
        'hr',
        'delivery',
        'stock_picking_batch',
        'purchase_requisition',
        'board',
        'knowledge',
        'sale_margin'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/config.xml'
    ],
    # only loaded in demonstration mode
    # 'demo': [
        # 'demo/demo.xml',
    # ],
}
