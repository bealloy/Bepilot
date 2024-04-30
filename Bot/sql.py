import sqlite3

conn = sqlite3.connect('Taipy.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    email TEXT)''')

cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('JohnDoe', 'john@example.com'))

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()
