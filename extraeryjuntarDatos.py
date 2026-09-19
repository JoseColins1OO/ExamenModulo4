import pandas as pd

script_code = """
import requests
import pandas as pd

# Descarga archivos en linea
url = 'https://raw.githubusercontent.com/anaepm/rep/refs/heads/main/nobel_personal.csv'
df1 = pd.read_csv(url)
url2= "https://raw.githubusercontent.com/anaepm/rep/refs/heads/main/nobel_data.csv"
df2 = pd.read_csv(url2)

# JOIN entre los 2 conjunto de datos
dfcompleto = pd.merge(df1, df2, on=['Firstname', 'Lastname'])
dfcompleto.head()

#Convertir a DataFrame
df = pd.DataFrame(datos)
df.to_csv("PremiosNOVEL.csv", index=False)
print("archivo PremiosNOVEL.csv creado.")
"""
