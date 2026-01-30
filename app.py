import streamlit as st
import pandas as pd
from database import init_db
from logic import obtener_proyectos, insertar_proyecto

st.set_page_config(page_title="Gestión de Recursos", layout="wide")

init_db()

st.title("📊 Gestión de Proyectos y Recursos")

with st.form("nuevo_proyecto"):
    st.subheader("➕ Nuevo Proyecto")

    codigo = st.text_input("Código del proyecto")
    nombre = st.text_input("Nombre del proyecto")
    estado = st.selectbox(
        "Estado",
        ["Por confirmar", "Confirmado", "Cancelado", "Reprogramado", "Postergado"]
    )
    inicio = st.date_input("Fecha inicio")
    fin = st.date_input("Fecha fin")

    guardar = st.form_submit_button("Guardar proyecto")

    if guardar:
        insertar_proyecto(codigo, nombre, estado, str(inicio), str(fin))
        st.success("Proyecto registrado correctamente")

st.divider()

st.subheader("📋 Proyectos registrados")
df = obtener_proyectos()

if df.empty:
    st.info("No hay proyectos aún")
else:
    st.dataframe(df, use_container_width=True)

    conteo = df["estado"].value_counts()
    st.subheader("📈 Estado de proyectos")
    st.bar_chart(conteo)
