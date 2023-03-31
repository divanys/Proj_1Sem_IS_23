import sqlite3 as sq
from data import info_users
from data import info_games

with sq.connect('DB/saper.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
        )""")
    # cur.execute("INSERT INTO users VALUES (6, 'Марк', 1, 18, 700)")

    # cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)",  info_users)

with sq.connect('DB/saper.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS games (
        games_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        score INTEGER,
        time INTEGER
        )""")

    # cur.executemany("INSERT INTO games VALUES (?, ?, ?, ?)",  info_games)

with sq.connect('DB/saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM games")
    result = cur.fetchall()
print(result)

with sq.connect('DB/saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM games WHERE score < 3000 ")
    result1 = cur.fetchall()
print(result1)

with sq.connect('DB/saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM games WHERE time < 3000 ")
    result2 = cur.fetchall()
print(result2)

with sq.connect('DB/saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM games WHERE games_id = 2 ")
    result3 = cur.fetchall()
print(result3)

with sq.connect('DB/saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM games WHERE score = 700")
    result4 = cur.fetchall()
print(result4)

with sq.connect('DB/saper.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE games SET score = score+300 WHERE score = 1000 ")
    result5 = cur.fetchall()

with sq.connect('DB/saper.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE games SET time = time+300 WHERE score = 1000 ")
    result6 = cur.fetchall()

with sq.connect('DB/saper.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM games WHERE user_id = 1")
    result7 = cur.fetchall()
    cur.execute("SELECT * FROM games")
    result7_1 = cur.fetchall()
print(result7_1)