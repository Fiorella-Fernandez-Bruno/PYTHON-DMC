import streamlit as st
import numpy as np
import pandas as pd

from libreria_funciones_proyecto1 import calcular_margen_neto
from librería_clases_proyecto1 import InventarioProducto

st.set_page_config(page_title="Proyecto 1 - Python Fundamentals", page_icon="🐍")
st.sidebar.image("DMC.png")
st.sidebar.title("Navegación")
seccion = st.sidebar.selectbox("Selecciona una sección", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
if seccion == "Home":
    st.title("Proyecto Aplicado - Python Fundamentals")
    st.subheader("Especialización en Python for Analytics")
    st.write("Elaborado por Fiorella Fernandez")

    st.image("Fiorella.jpeg", width=200)

    st.markdown("**Nombre completo:** Fiorella Fernandez Bruno")
    st.markdown("**Módulo:** Módulo 1 - Python Fundamentals")
    st.markdown("**Año:** 2026")

    st.markdown("""
    ### Descripción del proyecto
    Esta aplicación integra los conceptos fundamentales del Módulo 1 del curso:
    variables, estructuras de datos, control de flujo, funciones, programación
    funcional y programación orientada a objetos (POO), mediante una interfaz
    interactiva construida con **Streamlit**.

    ### Tecnologías utilizadas
    - Python 3
    - Streamlit
    - NumPy
    - Pandas
    """)

elif seccion == "Ejercicio 1":
    st.title("Ejercicio 1 - Flujo de caja con listas")
    st.markdown("Registra tus movimientos financieros (ingresos y gastos) y visualiza el flujo de caja resultante.")
    
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, value=0.0, step=0.01)
   
    if st.button("Agregar movimiento"):
        if concepto.strip() == "":
            st.error("Ingresa un concepto válido.")
        elif valor <= 0:
            st.error("El valor debe ser mayor que cero.")
        else:
            st.session_state.movimientos.append({"Concepto": concepto, "Tipo": tipo, "Valor": valor})
            st.success(f"Movimiento '{concepto}' agregado correctamente.")

    if st.session_state.movimientos:
        st.subheader("Movimientos registrados")
        st.dataframe(st.session_state.movimientos)

        total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
        total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos

        col1, col2, col3 = st.columns(3)
        col1.metric("Total ingresos", f"S/ {total_ingresos:,.2f}")
        col2.metric("Total gastos", f"S/ {total_gastos:,.2f}")
        col3.metric("Saldo final", f"S/ {saldo_final:,.2f}")
        
        if saldo_final >= 0:
            st.success("El flujo de caja está a favor.")
        else:
            st.error("El flujo de caja está en contra.")
    else:
        st.info("Aún no has registrado movimientos.")

