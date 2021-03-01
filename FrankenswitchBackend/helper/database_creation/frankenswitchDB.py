from db_helper import create_db, get_cursor

def create_frankenswitchDB():
    cursor = get_cursor()
    # create_db(cursor, "frankenswitch")
    create_tables(cursor)


def create_tables(cursor):
    cursor.execute("CREATE TABLE frankenswitch ("
                   "top VARCHAR ( 50 ) REFERENCES top(name),"
                   "stem VARCHAR ( 50 ) REFERENCES stem(name),"
                   "bottom VARCHAR ( 50 ) REFERENCES bottom(name),"
                   "spring VARCHAR ( 50 ),"
                   "info TEXT,"
                   "UNIQUE(top, bottom, stem)"
                   ");")


# drop table bottom; drop table top; drop table spring; drop table stem;

create_frankenswitchDB()