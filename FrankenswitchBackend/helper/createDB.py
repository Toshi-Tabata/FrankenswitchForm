from psycopg2 import connect, extensions, sql
from switchDataParse import get_switch_info
import json

with open('token.json') as f:
    data = json.load(f)
    print(data)
    password = data["password"]
    user = data["user"]


DB_NAME = "blacklist_combo"
conn = connect(
    dbname=DB_NAME,
    user=user,
    host="localhost",
    password=password,
    port="5432"
)

cursor = conn.cursor()
autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
conn.set_isolation_level(autocommit)


def create_db(name):
    # cursor.execute("CREATE DATABASE " + DB_NAME)  # avoiding string formats due to sqli
    cursor.execute(sql.SQL(
        "CREATE DATABASE {}"
    ).format(sql.Identifier(name)))


def create_tables():
    cursor.execute("CREATE TABLE manufacturer ("
                   "name VARCHAR ( 50 ) UNIQUE NOT NULL"
                   ");")

    cursor.execute("CREATE TABLE Top ("
                   "name VARCHAR ( 50 ) UNIQUE NOT NULL,"
                   "manufacturer VARCHAR ( 50 ) REFERENCES manufacturer(name)"
                   ");")
    cursor.execute("CREATE TABLE bottom ("
                   "name VARCHAR ( 50 ) UNIQUE NOT NULL,"
                   "manufacturer VARCHAR ( 50 ) REFERENCES manufacturer(name)"
                   ");")
    cursor.execute("CREATE TABLE Stem ("
                   "name VARCHAR ( 50 ) UNIQUE NOT NULL,"
                   "manufacturer VARCHAR ( 50 ) REFERENCES manufacturer(name)"
                   ");")

    cursor.execute("CREATE TABLE Blacklist ("
                   "top VARCHAR ( 50 ) REFERENCES top(name),"
                   "bottom VARCHAR ( 50 ) REFERENCES bottom(name),"
                   "stem VARCHAR ( 50 ) REFERENCES stem(name), UNIQUE(top, bottom, stem)"
                   ");")

    cursor.execute("ALTER TABLE blacklist "
                   "ADD CONSTRAINT OnlyOneNullColumn "
                   "CHECK ("
                   "( CASE WHEN top IS NULL THEN 0 ELSE 1 END"
                   "+ CASE WHEN bottom IS NULL THEN 0 ELSE 1 END"
                   "+ CASE WHEN stem IS NULL THEN 0 ELSE 1 END"
                   ") > 1"
                   ");")

    # cursor.execute("INSERT INTO Top(name) VALUES ('gateron'), ('cherry'), ('jwk');")
    # cursor.execute("INSERT INTO Stem(name) VALUES ('gateron'), ('cherry'), ('jwk');")
    # cursor.execute("INSERT INTO Bottom(name) VALUES ('gateron'), ('cherry'), ('jwk');")
    # cursor.execute("INSERT INTO Blacklist(top, bottom, stem) VALUES ('gateron', 'jwk', 'cherry')")
    # cursor.execute("INSERT INTO Blacklist(top, bottom, stem) VALUES ('gateron', 'cherry', 'jwk')")


def populate_tables():
    # cursor.execute("DROP TABLE top, bottom, stem, blacklist, manufacturer;")
    create_tables()

    manufacturers, switchNames, variety = get_switch_info()
    for i in range(len(manufacturers)):
        manufacturer = manufacturers[i]
        if manufacturer:
            manufacturer = manufacturer[0].lower()
            cursor.execute(f"INSERT INTO manufacturer (name) VALUES('{manufacturer}') "
                           f"ON CONFLICT(name) DO UPDATE SET name = EXCLUDED.name;")

        switchName = switchNames[i]
        v = variety[i] if i < len(variety) else None
        if switchName:
            switchName = switchName[0].lower() + " " + v[0].lower() if v else switchName[0].lower()
            manufacturer = manufacturer if manufacturer else None
            query = "INSERT INTO top (name, manufacturer) VALUES(%s, %s) " \
                    "ON CONFLICT(name) DO UPDATE SET name = EXCLUDED.name"
            cursor.execute(query, (switchName, manufacturer))
            query = "INSERT INTO bottom (name, manufacturer) VALUES(%s, %s) " \
                    "ON CONFLICT(name) DO UPDATE SET name = EXCLUDED.name"
            cursor.execute(query, (switchName, manufacturer))
            query = "INSERT INTO stem (name, manufacturer) VALUES(%s, %s) " \
                    "ON CONFLICT(name) DO UPDATE SET name = EXCLUDED.name"
            cursor.execute(query, (switchName, manufacturer))


# cursor.execute("DROP TABLE top, bottom, stem, blacklist, manufacturer;")
# populate_tables()
cursor.execute("SELECT * FROM top;")
print(cursor.fetchall())


conn.commit()
cursor.close()
conn.close()



