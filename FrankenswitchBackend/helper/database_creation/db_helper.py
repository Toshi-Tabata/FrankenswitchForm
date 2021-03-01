from psycopg2 import connect, extensions, sql
import os
import json

def get_cursor():
    token = os.path.split(os.path.dirname(__file__))[0]
    with open(token + '/token.json') as f:
        data = json.load(f)
        password = data["password"]
        user = data["user"]

    conn = connect(
        dbname="frankenswitchform",
        user=user,
        host="localhost",
        password=password,
        port="5432"
    )

    cursor = conn.cursor()
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    conn.set_isolation_level(autocommit)

    return cursor

def create_db(cursor, name):
    # cursor.execute("CREATE DATABASE " + DB_NAME)  # avoiding string formats due to sqli
    cursor.execute(sql.SQL(
        "CREATE DATABASE {};"
    ).format(sql.Identifier(name)))


