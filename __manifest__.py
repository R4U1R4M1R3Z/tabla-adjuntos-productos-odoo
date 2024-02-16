{
    'name': 'Attachment product',
    'version': '1.0',
    'description': 'Modulo personalizado para tener una tabla con adjuntos en el modelo product.template',
    'author': 'Raúl Ramírez',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Custom',
    'depends': ['base', 'product'],
    'data': [
        'views/product_template_custom_views.xml',
        'views/attachment.xml',
    ],
    'demo': [],
    'auto_install': False,
    'application': True,
}