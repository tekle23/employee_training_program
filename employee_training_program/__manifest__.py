{
    'name': "Employee Training Program",
    'version': "16.0.0.1",
    'summary': """ HR Department module""",
    'description': """holds all hr module features""",
    'author': "Smart ERP Team",
    'company': "Ashewa Technology Solutions",
    'maintainer': "Ashewa Technology Solutions",
    'website': "https://www.ashewa.com",
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
    # 'icon': 'static/description/icon/icon.png',
}
