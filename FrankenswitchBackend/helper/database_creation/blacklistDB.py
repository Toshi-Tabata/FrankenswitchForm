from db_helper import create_db, get_cursor
from switchDataParse import get_switch_info, insert_frankenswitch
from accessDB import add_blacklist
"""
Before running anything, make a PostgreSQL database (in psql):

CREATE DATABASE frankenswitchform;
CREATE USER username WITH ENCRYPTED PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE frankenswitchform TO username;
ALTER USER username CREATEDB;

Create a token.json file containing
{
    "user": "username",
    "password": "yourpassword"
}

Call create_blacklistDB() to create and populate the required tables
"""


def create_blacklistDB():
    cursor = get_cursor()
    create_db(cursor, "blacklist")
    create_tables(cursor)
    populate_tables(cursor)
    fill_blacklist(cursor)


# Note: There's a table for each part instead of a singular table since I think it's nicer to manage
# and switch parts get sold individually instead of as a switch
def create_tables(cursor):
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

def populate_tables(cursor):
    # cursor.execute("DROP TABLE top, bottom, stem, blacklist, manufacturer;")

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


# Fills blacklist TABLE with known blacklisted combinations.
# Currently hardcoded for panda/outemu/mod/cherry/outemu switch combinations.
# TODO: allow blacklist submissions and get more blacklisted combinations from community
def fill_blacklist(cursor):
    cursor.execute("SELECT * FROM top WHERE name LIKE '%panda%' AND manufacturer LIKE 'bsun%';")
    cursor.execute("SELECT * FROM top WHERE manufacturer='outemu';")
    bottoms = cursor.fetchall()

    cursor.execute("SELECT * FROM bottom WHERE name LIKE 'mod%';")
    cursor.execute("SELECT * FROM top WHERE manufacturer='cherry';")
    cursor.execute("SELECT * FROM top WHERE manufacturer='outemu';")

    tops = cursor.fetchall()

    for top in tops:
        for bottom in bottoms:
            add_blacklist(top[0], None, bottom[0], cursor)

