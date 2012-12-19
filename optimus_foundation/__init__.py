"""
This is an Optimus template project for Foundation, the version will follow the version of Foundation
"""
__version__ = "3.2.3"

# Directory structure to create
DIRECTORY_STRUCTURE = [
    # list(dir_name[, children_dir_list])
    [
        'sources',
        [
            ['js'],
            ['css'],
            ['scss'],
            ['images'],
            ['templates'],
        ]
    ]
]

# Script template files
# NOTE: Files are rendered with the ``String.format()`` method, so remember to double 
#       all your '{' and '}', else they will be interpreted as format variable, and 
#       probably raise a Key error
SCRIPT_FILES = [
    ['requirements.txt', 'requirements.txt'],
    ['gemsets.txt', 'gemsets.txt'],
    ['README.rst', 'README.rst'],
    # Default scripts
    ['scripts/__init__.py.tpl', '__init__.py'],
    ['scripts/settings.py.tpl', 'settings.py'],
    ['scripts/prod_settings.py.tpl', 'prod_settings.py'],
    ['scripts/pages.py.tpl', 'pages.py'],
    ['scripts/config.rb.tpl', 'config.rb'],
    # Default sources
    ['sources/templates/base.html', 'sources/templates/base.html'],
    ['sources/templates/index.html', 'sources/templates/index.html'],
    ['sources/templates/readme.html', 'sources/templates/readme.html'],
    ['sources/css/app.css', 'sources/css/app.css'],
]
