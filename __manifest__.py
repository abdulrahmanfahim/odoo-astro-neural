{
    'name': 'Astro Neural Network',
    'version': '1.71',
    'author': 'Abdulrahman Fahim',
    'website': 'https://abdulrahmanfahim.github.io',
    'category': 'Website/Neural',
    'summary': 'Geometric neural network background + dark/light mode toggle in navbar',
    'description': """
        Transform your Odoo website with a stylish geometric neural network background.
        This module replaces the default website background with an eye‑catching,
        customizable neural network pattern. Additionally, it adds a convenient
        toggle button directly in the navbar, allowing visitors to switch between
        dark and light mode with a single click. Perfect for tech‑savvy sites or
        anyone wanting a modern, dynamic look.
        
        Key Features:
        • Dynamic neural network background (configurable colors/patterns)
        • Dark/light mode toggle integrated into the main navigation bar
        • Fully responsive and compatible with Odoo’s website builder
        • Lightweight and easy to install
    """,
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views.xml',
    ],
    'images': [
        'static/description/icon.png',
        'static/description/screenshot1.png',  # Your main screenshot
        'static/description/screenshot2.png',  # Additional screenshot
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 29.99,
    'currency': 'USD',
}
