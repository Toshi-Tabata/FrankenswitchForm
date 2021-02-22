from psycopg2 import connect, extensions, sql
from switchDataParse import get_switch_info, insert_frankenswitch
import os
import json


token = os.path.split(os.path.dirname(__file__))[0]
with open(token + '/helper/token.json') as f:
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

def add_blacklist(top, stem, bottom):
    cursor.execute("INSERT INTO blacklist(top, stem, bottom) VALUES (%s, %s, %s);", (top, stem, bottom))


def fill_blacklist():
    cursor.execute("SELECT * FROM top WHERE name LIKE '%panda%' AND manufacturer LIKE 'bsun%';")
    cursor.execute("SELECT * FROM top WHERE manufacturer='outemu';")
    bottoms = cursor.fetchall()

    cursor.execute("SELECT * FROM bottom WHERE name LIKE 'mod%';")
    cursor.execute("SELECT * FROM top WHERE manufacturer='cherry';")
    cursor.execute("SELECT * FROM top WHERE manufacturer='outemu';")

    tops = cursor.fetchall()

    for top in tops:
        for bottom in bottoms:
            add_blacklist(top[0], None, bottom[0])

# fill_blacklist()  # run this if you need to populate blacklist again

def get_switches():
    cursor.execute("SELECT * FROM top;")
    switches = cursor.fetchall()

    res = []
    for switch in switches:
        # TODO: this was short sighted since i need to undo this when it gets the info back. let frontend handle it?
        string = switch[1] + " " + switch[0] if switch[1] else switch[0]
        res.append(string)

    res.sort()
    return res

def submitCombo(top, stem, bottom):
    # silent white, phoenix
    print("checking", top, stem, bottom)
    cursor.execute("SELECT * FROM blacklist WHERE "
                   "(top, bottom) = (%s, %s) OR"
                   "(top, stem) = (%s, %s) OR"
                   "(stem, bottom) = (%s, %s);", (top, bottom, top, stem, stem, bottom))

    found = cursor.fetchall()
    if len(found) > 0:
        # TODO: handle error
        invalid = [part for part in found[0] if part is not None]
        msg = "Invalid combo with "
        msg += ', '.join(invalid)
        return msg
    else:
        # TODO: add to spreadsheet
        insert_frankenswitch(top, stem, bottom)
        return ""


def close():
    conn.commit()
    cursor.close()
    conn.close()



