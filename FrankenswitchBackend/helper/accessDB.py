from switchDataParse import get_switch_info, insert_frankenswitch

# cursor.execute("DROP TABLE top, bottom, stem, blacklist, manufacturer;")
# populate_tables()

def add_blacklist(top, stem, bottom, cursor):
    cursor.execute("INSERT INTO blacklist(top, stem, bottom) VALUES (%s, %s, %s);", (top, stem, bottom))


def get_switches(cursor):
    cursor.execute("SELECT * FROM top;")
    switches = cursor.fetchall()

    res = []
    for switch in switches:
        manu = switch[1] if switch[1] is not None else "None"
        data = {
            "manufacturer": manu,
            "name": switch[0]
        }
        res.append(data)

    # res.sort()
    return res


def submitCombo(top, stem, bottom, cursor, info):
    # e.g. silent white, phoenix should get blacklisted
    topName = top["name"]
    stemName = stem["name"]
    bottomName = bottom["name"]
    top = f"{top['manufacturer']} {top['name']}"
    stem = f"{stem['manufacturer']} {stem['name']}"
    bottom = f"{bottom['manufacturer']} {bottom['name']}"
    cursor.execute("SELECT * FROM blacklist WHERE "
                   "(top, bottom) = (%s, %s) OR"
                   "(top, stem) = (%s, %s) OR"
                   "(stem, bottom) = (%s, %s);", (topName, bottomName, topName, stemName, stemName, bottomName))
    found = cursor.fetchall()
    cursor.execute("SELECT * FROM frankenswitch WHERE "
                   "(top, stem, bottom) = (%s, %s, %s);", (topName, stemName, bottomName))
    was_made = cursor.fetchall()

    if len(found) > 0:
        invalid = [part for part in found[0] if part is not None]
        msg = "Invalid combo with "
        msg += ', '.join(invalid)
        return msg
    elif was_made:
        return "Switch has already been submitted"
    else:
        success = add_frankenswitch(topName, stemName, bottomName, cursor)
        if success:
            insert_frankenswitch(top, stem, bottom, info)
            return ""
        else:
            return "failed to insert into database"


def add_frankenswitch(top, stem, bottom, cursor):
    query = "INSERT INTO frankenswitch (top, stem, bottom) VALUES(%s, %s, %s);"
    try:
        cursor.execute(query, (top, stem, bottom))
        return True
    except Exception as e:
        print("Insert failed. Ignoring and continuing. Error was: ", e)
        return False




