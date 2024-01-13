import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Empleatronix")
st.write('Todos los datos sobre los empleados en una aplicación')

# Carga del csv
empleados = pd.read_csv("data/employees.csv")

# Mostramos el Dataframe
st.dataframe(empleados)

# Dividimos las partes
st.divider()

# Creamos una columna con los botones para el color, nombre y el sueldo de nuestro grafico

col1, col2, col3 = st.columns(3)

with col1:
    color = st.color_picker('Elige un color para las barras', '#3475B3')

with col2:
    nombre = st.toggle('Mostrar el nombre')

with col3:
    sueldo = st.toggle('Mostrar sueldo en la barra')

# Creamos el grafico de barras
fig, ax = plt.subplots()

# Añadir los nombres y los sueldos a las barras si los toggles son True
if nombre:
    ax.barh(empleados['full name'], empleados['salary'], color=color)
else:
    ax.barh(np.arange(len(empleados)), empleados['salary'], color=color)

if sueldo:
    for i, s in enumerate(empleados['salary']):
        ax.text(s + 50, i - 0.3, str(s) + '€', color='black')

# Ajusta el rango del eje x
ax.set_xlim([0, 4500])

# Muestra el grafico en Streamlit
st.pyplot(fig)

st.write('Elena Racero González - CPIFP Alan Turing')