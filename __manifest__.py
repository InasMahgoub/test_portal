# -*- coding: utf-8 -*-
{
    'name': "Portal",
    'summary': "Portal",
    'description': "Portal",
    'author': "Inas Mahgoub",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Portal',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'portal', 'website', 'web'],


    # always loaded
    'data': [
        'views/templates.xml',
        'views/views.xml',
        # 'views/expenses.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

'assets': {
        "web.assets_frontend": {
            
            'https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css',
            'test_portal/static/src/scss/bootstrap.extend.scss',
            'test_portal/static/src/scss/portal.scss',
            "test_portal/static/src/css/style.css",
            'https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js',
            'test_portal/static/src/js/portal.js',
            'test_portal/static/src/js/portal_chatter.js',
            'test_portal/static/src/js/portal_composer.js',
            'test_portal/static/src/js/portal_signature.js',
            'test_portal/static/src/js/portal_sidebar.js',
            'https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap',
            'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css'
            
        }
    },
    'application': True,
    'sequence': -110
}
