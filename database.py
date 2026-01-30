import sqlite3

DB_NAME = "recursos.db"

def conectar():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def crear_tablas():
    conn = conectar()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS personal (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        cargo TEXT,
        area TEXT,
        disponible INTEGER DEFAULT 1
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS proyectos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT,
        nombre TEXT,
        estado TEXT,
        fecha_inicio TEXT,
        fecha_fin TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS asignaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        personal_id INTEGER,
        proyecto_id INTEGER
    )
    """)

    conn.commit()
    conn.close()

