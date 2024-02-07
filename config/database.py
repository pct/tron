from masoniteorm.query import QueryBuilder
from masoniteorm.connections import ConnectionResolver

DATABASES = {
    'default': 'mysql',
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'tron',
        'prefix': '',
        'port': 3306,
        'options': {
            'charset': 'utf8mb4',
        },
    },
}

DB = ConnectionResolver().set_connection_details(DATABASES)

