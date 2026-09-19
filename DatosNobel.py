import requests

# Guardar el script completo en un archivo DatosNobel.py local
script_code = """ 
import requests
import pandas as pd

#1. importar conjuntos de datos
url = 'https://raw.githubusercontent.com/anaepm/rep/refs/heads/main/nobel_personal.csv'
df1 = pd.read_csv(url)
url2= "https://raw.githubusercontent.com/anaepm/rep/refs/heads/main/nobel_data.csv"
df2 = pd.read_csv(url2)

#2. merge conjunto de datos
dfcompleto = pd.merge(df1, df2, on=['Firstname', 'Lastname'])

#3. convertir a CSV
dfcompleto.to_csv('nobel.csv', index=False)
print("archivo catalogo_libros.csv creado.")

"""
