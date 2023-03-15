from sqlite3 import *
players = [[12, 'Николай', 1, 24, 1500],
           [13, 'Михаил', 1, 22, 1200],
           [14, 'Мария', 2, 18, 500],
           [15, 'Евгения', 2, 29, 1700],
           [16, 'Григорий', 1, 18, 2500]]
with connect('DB/Saper.db') as db:
    cur = db.cursor()
#     cur.executemany(f"INSERT INTO users VALUES (?, ?, ? ,?, ?)", players)
    cur.execute("SELECT * FROM users")
    all_players = cur.fetchall()
    print(f"Все игроки: \n{all_players}")

    print(cur.execute(f"SELECT * FROM users WHERE sex='2'").fetchall())
    print(cur.execute(f"SELECT * FROM users WHERE score < 1000").fetchall())
    print(cur.execute(f"SELECT * FROM users ORDER BY score DESC").fetchone())
    print(cur.execute(f"SELECT * FROM users WHERE old BETWEEN 18 AND 20").fetchall())

    cur.execute(f"UPDATE users SET old = 20 WHERE old = 19")
    cur.execute(f"UPDATE users SET score=score+300 WHERE score < 1000")
    cur.execute(f"UPDATE users SET score = score + 100 WHERE old >= 20")
    cur.execute(f"DELETE FROM users WHERE score <= 1000")