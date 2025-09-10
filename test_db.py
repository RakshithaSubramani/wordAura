import sqlite3
import pandas as pd

DB_PATH = "stories.db"  # Adjust if using absolute path
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stories
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              prompt TEXT NOT NULL,
              genre TEXT,
              length INTEGER,
              story TEXT NOT NULL,
              timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
c.execute("INSERT INTO stories (prompt, genre, length, story) VALUES (?, ?, ?, ?)",
          ("Test prompt", "Fantasy", 300, "This is a test story."))
conn.commit()
print(pd.read_sql_query("SELECT * FROM stories", conn))
conn.close()