import sqlite3


def create_table() -> None:
    con = sqlite3.connect('phones.db')
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    phones_db = '''CREATE TABLE users (
    "UID" INTEGER PRIMARY KEY AUTOINCREMENT,
	"UNAME" TEXT,
	"CONTACT" TEXT
)'''
    cur.execute(phones_db)
    con.commit()
    con.close()
