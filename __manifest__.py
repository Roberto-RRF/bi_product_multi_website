# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{

    'name': "Product Multi Website | Allow Products on Multi Website",
    'version': '17.0.0.0',
    'category': 'eCommerce',
    'summary': 'Product on multi website product selection on website choose product on website product multi eCommerce product multi shop allow product on multi website product different website selection manage product on multi website per product multiple website shop',
    'description': """
      
        Product Multi Website in odoo,
        Multi Website for Each Product in odoo,
        Set Multiple Websites for Product in odoo,
        Mass Update Product Websites in odoo,
        Update Multiple Product website in odoo,
        Product Website in odoo,
    
    """,
    'author': 'BROWSEINFO',
    "price": 35,
    "currency": 'EUR',
    'website': "https://www.browseinfo.com/demo-request?app=bi_product_multi_website&version=17&edition=Community",
    'depends': ['base', 'website','website_sale','product','sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/mass_update_product_views.xml',
    ],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'live_test_url':"https://www.browseinfo.com/demo-request?app=bi_product_multi_website&version=17&edition=Community",
    "images":['static/description/Banner.gif'],
}
