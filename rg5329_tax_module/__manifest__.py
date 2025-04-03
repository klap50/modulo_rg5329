### Estructura de un módulo Odoo para crear el impuesto RG 5329 ###

# __manifest__.py
{
    'name': 'Impuesto Percepción RG 5329',
    'version': '1.0.0',
    'category': 'Accounting',
    'summary': 'Crea el impuesto de percepción RG 5329 (AFIP)',
    'author': 'Tu Nombre o Empresa',
    'website': 'https://tusitio.com',
    'license': 'LGPL-3',
    'depends': ['account'],
    'data': [
        'data/rg5329_tax.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}

