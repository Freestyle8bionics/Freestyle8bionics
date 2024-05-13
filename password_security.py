import sqlite3
import hashlib


conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
            
)
""")

username1, password1 = "connor942", hashlib.sha256("connorpassword392".encode("utf-8")).hexdigest()
username2, password2 = "myaccount123", hashlib.sha256("myP4s5w0rd".encode("utf-8")).hexdigest()
username3, password3 = "otheraccount", hashlib.sha256("0tHerP4s5W()rd".encode("utf-8")).hexdigest()
username4, password4 = "oldman", hashlib.sha256("oldhackers".encode("utf-8")).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()
