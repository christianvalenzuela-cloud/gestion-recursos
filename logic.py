import pandas as pd
from database import get_connection

def obtener_proyectos():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM proyectos", conn)
    conn.close()
    return df

def insertar_proyecto(codigo, nombre, estado, inicio, fin):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO proyectos (codigo, nombre, estado, fecha_inicio, fecha_fin) VALUES (?,?,?,?,?)",
        (codigo, nombre, estado, inicio, fin)
    )
    conn.commit()
    conn.close()
