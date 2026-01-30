from database import conectar, crear_tablas

personal = [
    ("Cinthya Bellido", "Administradora", "Oficina"),
    ("Antonio Velasco", "Jefe de Servicios", "Servicios"),
    ("Christian Valenzuela", "Coord. Servicios", "Servicios"),
    ("Marco Subelete", "Coord. Servicios", "Servicios"),
    ("Juan Espinoza", "Ing. Comunicación", "Ingeniería"),
    ("Juan Pilco", "Ing. Sup. Servicios", "Ingeniería"),
    ("Wilber Chiclla", "Ing. Sup. Servicios", "Ingeniería"),
    ("Luis Flores", "Sup. Seguridad", "Seguridad"),
    ("Victor Salazar", "Sup. Seguridad", "Seguridad"),
    ("Lilian Huaman", "Sup. Seguridad", "Seguridad"),
    ("Tec. Juan Sunción", "Sup. Técnico", "Técnico"),
    ("Tec. Henry Sandoval", "Sup. Técnico", "Técnico"),
    ("Tec. Miguel Conyas", "Técnico", "Técnico"),
    ("Tec. Edinson Morales", "Técnico", "Técnico"),
    ("Tec. Luis Martinez", "Técnico", "Técnico"),
    ("Tec. Darwin Araujo", "Técnico / Rigger", "Técnico"),
    ("Tec. Christian Rivas", "Técnico", "Técnico"),
    ("Tec. Alex Palomino", "Técnico", "Técnico"),
    ("Tec. Percy Ugarte", "Técnico", "Técnico"),
    ("Tec. Saul Sotelo", "Técnico", "Técnico"),
    ("Tec. Taipe Opver", "Técnico", "Técnico"),
    ("Tec. Tito Melendez", "Técnico", "Técnico"),
    ("Tec. Danny Condor", "Técnico", "Técnico"),
    ("Tec. Karlo", "Técnico", "Técnico"),
    ("Tec. Deivis Rivera Guerrero", "Técnico", "Técnico"),
    ("Everly Tapia", "Conductor", "Movilidad"),
    ("Segundo Gícaro", "Camión Grúa", "Obras"),
    ("Wiler Coppa", "Coord. Servicios", "Arequipa"),
    ("Kelly Luna", "Sup. Seguridad", "Arequipa")
]

crear_tablas()
conn = conectar()
c = conn.cursor()

for nombre, cargo, area in personal:
    c.execute(
        "INSERT INTO personal (nombre, cargo, area, disponible) VALUES (?, ?, ?, 1)",
        (nombre, cargo, area)
    )

conn.commit()
conn.close()

print("✔ Personal cargado correctamente")

