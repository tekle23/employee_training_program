{
    'name': "Employee Training Program",
    'version': "16.0.0.1",
    'summary': """ HR Department module""",
    'description': """Manage employee training""",
    'author': "Tekle Yitayew",
    'company': "Odoo Ethiopia",
    'category': 'HR',
    'depends': ['base_setup', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'view/training_program.xml',
        'view/training_detail.xml',
        'view/institute_view.xml',
        'view/menu_items.xml',
    ],

    'license': "AGPL-3",
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
}
