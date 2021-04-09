import accessDB as adb
from db_helper import get_cursor

top = {
    "name": "'foo' or true; drop table blacklist; -- ",
    "manufacturer": "'foo' or true; drop table blacklist; -- "
}
stem = {
    "name": "'foo' or true; drop table blacklist; -- ",
    "manufacturer": "'foo' or true; drop table blacklist; -- "
}
bottom = {
    "name": "'foo' or true; drop table blacklist; -- ",
    "manufacturer": "'foo' or true; drop table blacklist; -- "
}

adb.submitCombo(top, stem, bottom, get_cursor(), {})


