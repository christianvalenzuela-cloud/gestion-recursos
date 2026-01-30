import sqlite3
from database import conectar

# -------- PERSONAL --------
def agregar_personal(codigo, nombre, rol):
    conn = conectar()
    c = conn.cursor()
    c.execute(
        "INSERT INTO personal (codigo, nombre, rol) VALUES (?, ?, ?)",
        (codigo, nombre, rol)
    )
    conn.commit()
    conn.close()

def obtener_personal():
    conn = conectar()
    c = conn.cursor()

    c.execute("""
    SELECT p.id, p.nombre,
    CASE
        WHEN EXISTS (
            SELECT 1 FROM asignaciones a
            WHERE a.personal_id = p.id
        )
        THEN 'Ocupado'
        ELSE 'Disponible'
    END estado
    FROM personal p
    """)

    data = c.fetchall()
    conn.close()
    return data

# -------- PROYECTOS --------
def agregar_proyecto(codigo, nombre, estado, inicio, fin):
    conn = conectar()
    c = conn.cursor()
    c.execute(
        "INSERT INTO proyectos (codigo, nombre, estado, fecha_inicio, fecha_fin) VALUES (?, ?, ?, ?, ?)",
        (codigo, nombre, estado, inicio, fin)
    )
    conn.commit()
    conn.close()

def obtener_proyectos():
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT id, nombre FROM proyectos")
    data = c.fetchall()
    conn.close()
    return data

# -------- ASIGNACIONES --------
def asignar_personal(personal_id, proyecto_id):
    conn = conectar()
    c = conn.cursor()
    c.execute(
        "INSERT INTO asignaciones (personal_id, proyecto_id) VALUES (?, ?)",
        (personal_id, proyecto_id)
    )
    conn.commit()
    conn.close()
