import streamlit as st
st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por Fiorella Fernández")
modulos = st.selectbox("Seleccione el módulo",["Listas","Arreglos","Funciones","POO"])
if modulos : "Listas"
 st.write("Te encuentras en el módulo de Listas")
elif modulos : "Arreglos"
  st.write("Te encuentras en el módulo de Arreglos")
elif modulos : "Funciones"
  st.write("Te encuentras en el módulo de Funciones")
else:
  st.write("Te encuentras en el módulo de POO")
