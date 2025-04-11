import sqlite3

DB_NAME = "shortcuts.db"

def create_table():
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shortcuts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            text TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

def add_shortcut(key, text):
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM shortcuts WHERE key = ?", (key,))
        existing_shortcut = cursor.fetchone()
        
        if existing_shortcut:
            print(f"Atalho '{key}' já existe, atualizando texto...")
            cursor.execute("UPDATE shortcuts SET text = ? WHERE key = ?", (text, key))
        else:
            cursor.execute("INSERT INTO shortcuts (key, text) VALUES (?, ?)", (key, text))
        
        conn.commit()
    
    except sqlite3.Error as e:
        print(f"Erro ao adicionar/atualizar atalho: {e}")
    
    finally:
        conn.close()

def get_shortcuts():
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT key, text FROM shortcuts")
    shortcuts = cursor.fetchall()
    
    conn.close()
    return shortcuts

def update_shortcut(key, new_text):
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE shortcuts SET text = ? WHERE key = ?", (new_text, key))
    conn.commit()
    conn.close()

def delete_shortcut(key):
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM shortcuts WHERE key = ?", (key,))
    conn.commit()
    conn.close()

create_table()
