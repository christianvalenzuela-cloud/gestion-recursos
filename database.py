import sqlite3
import os

DB_PATH = "data/recursos.db"

def conectar():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def crear_tablas():
    conn = conectar()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS personal (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT UNIQUE,
        nombre TEXT,
        rol TEXT
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
