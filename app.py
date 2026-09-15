import streamlit as st
import numpy as np

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por Fiorella Fernández")

st.image("Python_logo.png",width=300)
st.sidebar.image("DMC.png")

modulos = st.sidebar.selectbox("Seleccione el módulo",["Listas","Arreglos","Funciones","POO"])

if modulos == "Listas":
 st.write("Te encuentras en el módulo de Listas")
 valor_inicial = st.number_input("Ingresa tu valor inicial del rango",value=0)
 valor_final = st.number_input("Ingresa tu valor final del rango",value=10)
 Lista = list(range(valor_inicial,valor_final))
 st.write(Lista)


elif modulos == "Arreglos":
  st.write("Te encuentras en el módulo de Arreglos")
  cantidad = st.slider("Seleccione un valor del rango", min_value = 1, max_value = 100, value = 20)
  arreglo = np.arange(cantidad)
  st.write(arreglo)
elif modulos == "Funciones":
  st.write("Te encuentras en el módulo de Funciones")
else:
  st.write("Te encuentras en el módulo de POO")
 

