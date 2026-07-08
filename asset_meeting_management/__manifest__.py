{
    'name': 'Asset & Meeting Management',
    'version': '15.0.1.0.0',
    'summary': 'Quản lý tài sản và phòng họp',
    'description': """
        Quản lý tài sản
        Quản lý phòng họp
        Đặt phòng
        Lịch sử sử dụng
        Dashboard thống kê
            """,

    'author': 'Hoang Nhat',
    'website': '',
    'license': 'LGPL-3',

    'category': 'Administration',

    'depends': [
        'base',
        'mail',
        'hr',
    ],

    'data': [

        'security/security.xml',
        'security/ir.model.access.csv',

        'views/category_views.xml',
        'views/asset_views.xml',
        'views/room_views.xml',
        'views/booking_views.xml',
        'views/history_views.xml',
        'views/dashboard.xml',
        'views/menu.xml',

        'wizard/booking_wizard_view.xml',

        'demo/demo.xml',

    ],

    'application': True,
    'installable': True,
}

