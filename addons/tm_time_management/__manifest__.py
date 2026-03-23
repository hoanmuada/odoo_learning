# -*- coding: utf-8 -*-
{
    'name': 'Time Management',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/Time Management',
    'sequence': 80,
    'summary': 'Track and manage employee working time with approval workflow',
    'description': """
Time Management Module
======================
A comprehensive time tracking solution for managing employee work hours.

Features:
- Log daily time entries per project/task
- Categorize work (Development, Meeting, Training, etc.)
- Approval workflow: Draft → Submitted → Approved/Rejected
- Pivot & Graph reporting by employee, project, category
- Multi-level security: User / Manager / Admin
    """,
    'depends': ['hr', 'project'],
    'data': [
        'security/tm_security.xml',
        'security/ir.model.access.csv',
        'data/tm_data.xml',
        'views/tm_time_entry_views.xml',
        'views/tm_category_views.xml',
        'views/tm_menus.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
