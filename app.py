import streamlit as st
import numpy as np
import pandas as pd

from libreria_funciones_proyecto1 import calcular_margen_neto
from librería_clases_proyecto1 import InventarioProducto

st.set_page_config(page_title="Proyecto 1 - Python Fundamentals", page_icon="🐍")
st.sidebar.title("Navegación")
seccion = st.sidebar.selectbox("Selecciona una sección", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
st.sidebar.write("Elaborado por Fiorella Fernandez")
