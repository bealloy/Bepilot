import pandas as pd
from taipy.gui import Markdown, Gui
import mysql.connector

img = "setting_icon.png"
Lang = "English"

Host = None
User = None
passw = None
Connect = "Connect"

def connect_button(state):
  global Host, User, passw 

  Host = state.get("Host", None) 
  User = state.get("User", None)
  passw = state.get("passw", None) 

  if not (Host and User and passw):
    print("Error: Please enter all connection details (Host, User, Password).")
    return
  



  try:
    conn = mysql.connector.connect(
      host=Host,
      user=User,
      password=passw,
      database='Knowledge'
    )
    print("Successfully connected to MySQL database!")
    cursor.execute('''CREATE TABLE IF NOT EXISTS knowledge (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    filename VARCHAR(255),
                    description VARCHAR(255))''')

    cursor.execute("INSERT INTO knowledge (filename, description) VALUES (%s, %s)", ('File2.pdf', 'File2 Description'))

    cursor.execute("SELECT * FROM knowledge")
    rows = cursor.fetchall()

    for row in rows:
      print(row)

    cursor = conn.cursor()

    conn.commit()
    conn.close()

  except mysql.connector.Error as err:
    print("Error:", err)

setting_icon_ui = Markdown("web_pages/Setting_icon/setting_icon.md")
