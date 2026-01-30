from database import conectar, crear_tablas

crear_tablas()
conn = conectar()
c = conn.cursor()

personal = [
    ("Cinthya Bellido", "Administradora", "Administración"),
    ("Antonio Velasco", "Jefe de Servicios", "Servicios"),
    ("Christian Valenzuela", "Coord. Servicios", "Servicios"),
    ("Marco Subelete", "Coord. Servicios", "Servicios"),
    ("Juan Espinoza", "Ing. Comunicación", "Ingeniería"),
    ("Juan Pilco", "Ing. Sup. Servicios", "Ingeniería"),
    ("Wilber Chiclla", "Ing. Sup. Servicios", "Ingeniería"),
    ("Luis Flores", "Sup. Seguridad", "Seguridad"),
    ("Victor Salazar", "Sup. Seguridad", "Seguridad"),
    ("Lilian Huaman", "Sup. Seguridad", "Seguridad"),
    ("Juan Sunción", "Sup. Técnico", "Técnico"),
    ("Henry Sandoval", "Sup. Técnico", "Técnico"),
    ("Miguel Conyas", "Técnico", "Técnico"),
    ("Edinson Morales", "Técnico", "Técnico"),
    ("Luis Martinez", "Técnico", "Técnico"),
    ("Darwin Araujo", "Técnico / Rigger", "Técnico"),
    ("Christian Rivas", "Técnico", "Técnico"),
    ("Alex Palomino", "Técnico", "Técnico"),
    ("Percy Ugarte", "Técnico", "Técnico"),
    ("Saul Sotelo", "Técnico", "Técnico"),
    ("Taipe Opver", "Técnico", "Técnico"),
    ("Tito Melendez", "Técnico", "Técnico"),
    ("Danny Condor", "Técnico", "Técnico"),
    ("Karlo", "Técnico", "Técnico"),
    ("Deivis Rivera Guerrero", "Técnico", "Técnico"),
    ("Everly Tapia", "Conductor", "Movilidad"),
    ("Jorge Palomino", "Tercero", "Externo"),
    ("Llontop", "Personal Obras", "Obras"),
    ("Luis Morales M.", "Capataz Linero", "Obras"),
    ("Marcos Gaytán", "Capataz Electromecánico", "Obras"),
    ("Marco Guevara", "Técnico Electricista", "Obras"),
    ("Tadeo Vera", "Técnico Electricista", "Obras"),
    ("Fernando Moya", "Ing. Supervisor", "Ingeniería"),
    ("Victor Cardenas", "Ing. Supervisor", "Ingeniería"),
    ("Wiler Coppa", "Coord. Servicios", "Arequipa"),
    ("Christian Rodriguez", "Ing. Sup. Servicio", "Arequipa"),
    ("Kelly Luna", "Sup. Seguridad", "Arequipa")
]

c.executemany(
    "INSERT INTO personal (nombre, cargo, area) VALUES (?, ?, ?)",
    personal
)

conn.commit()
conn.close()

print("✅ Personal cargado correctamente")
