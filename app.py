import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por Fiorella Fernández")

modulos = st.sidebar.selectbox("Seleccione el módulo",["Listas","Arreglos","Funciones","POO"])

if modulos == "Listas":
 st.write("Te encuentras en el módulo de Listas")
 valor_inicial = st.number_input("Ingresa tu valor inicial del rango")
 valor_final = st.number_input("Ingresa tu valor final del rango")
elif modulos == "Arreglos":
  st.write("Te encuentras en el módulo de Arreglos")
elif modulos == "Funciones":
  st.write("Te encuentras en el módulo de Funciones")
else:
  st.write("Te encuentras en el módulo de POO")
 

