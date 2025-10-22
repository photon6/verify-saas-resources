{
    'name': 'LetsMeet',
    'version': '1.0',
    'summary': 'Calendly-style scheduling interface for Odoo',
    'description': 'A modern, user-friendly scheduling tool for booking meetings and appointments in Odoo.',
    'category': 'Productivity',
    'author': 'Propensic Solutions, LLC',
    'website': 'https://www.propensic.com',
    'depends': ['base', 'calendar', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/letsmeet_templates.xml',
        'views/letsmeet_views.xml',
        'data/default_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'letsmeet/static/src/js/letsmeet.js',
            'letsmeet/static/src/css/letsmeet.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
