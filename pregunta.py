"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    with open("clusters_report.txt", "r") as file:
        data = file.readlines()

    data = [linea.strip() for linea in data]

    data_slice = data[4:]
    pattern = r'^\s*(\d+)\s+(\d+)\s+([\d.,]+)\s*%\s*(.*)'

    full_data = []
    lista = []
    text = ""
    for line in data_slice:
        result = re.match(pattern, line)
        if result:
            lista = [int(result.group(1)), int(result.group(2)), float(result.group(3).replace(',', '.'))]
            text = result.group(4)
        else:
            text += ' ' + line.strip()

        if not line.strip():
            lista.append(text.strip())
            full_data.append(lista)
            lista = []
            text = ""

    col = ["Cluster", "Cantidad de palabras clave", "Porcentaje de palabras clave", "Principales palabras clave"]
    col = [column.lower().replace(" ", "_") for column in col]
    df = pd.DataFrame(full_data, columns=col)

    df["principales_palabras_clave"] = df["principales_palabras_clave"].str.replace(r"\.", "", regex=True)
    df["principales_palabras_clave"] = df["principales_palabras_clave"].str.replace(r"\s+", " ", regex=True)

    return df

# Llamada a la función para probarla
(ingest_data())

