"""
Example 3
Extension functions
"""

import pyexasol as E
import _config as config

import pprint
printer = pprint.PrettyPrinter(indent=4, width=140)

# Basic connect
C = E.connect(dsn=config.dsn, user=config.user, password=config.password, schema=config.schema, lower_ident=True)

cols = C.ext.get_columns('users')
printer.pprint(cols)

cols = C.ext.get_columns_sql('SELECT * FROM users')
printer.pprint(cols)

cols = C.ext.get_sys_columns('users')
printer.pprint(cols)

tables = C.ext.get_sys_tables()
printer.pprint(tables)

views = C.ext.get_sys_views()
printer.pprint(views)

schemas = C.ext.get_sys_schemas()
printer.pprint(schemas)

reserved_words = C.ext.get_reserved_words()
printer.pprint(reserved_words)