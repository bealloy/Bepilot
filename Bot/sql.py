import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456789',
    database='Knowledge'
)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS knowledge (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    filename VARCHAR(255),
                    description VARCHAR(255))''')

cursor.execute("INSERT INTO knowledge (filename, description) VALUES (%s, %s)", ('File.pdf', 'File Description'))

cursor.execute("SELECT * FROM knowledge")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()
