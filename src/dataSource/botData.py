import sqlite3

def newBotTable():
  conect = sqlite3.connect("src/botdata.db")
  cursor = conect.cursor()
  table = "CREATE TABLE IF NOT EXISTS Bot (id, token)" 
  cursor.execute(table)
  conect.commit()
  conect.close()
