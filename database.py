import sqlite3
import os

DB_PATH = "data/recursos.db"

def conectar():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def crear_tablas():
    conn = conectar()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS personal (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        cargo TEXT NOT NULL,
        area TEXT,
        disponible INTEGER DEFAULT 1
    )
    """)

    conn.commit()
    conn.close()

