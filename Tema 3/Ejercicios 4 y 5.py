# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 11:13:45 2026

@author: Mañana
"""

### EJERCICIO 4

import pandas as pd

# Leer los cuatro ficheros
emisiones_2017 = pd.read_csv("../Datasets/emisiones2016.csv", sep=";")
emisiones_2018 = pd.read_csv("../Datasets/emisiones2017.csv", sep=";")
emisiones_2019 = pd.read_csv("../Datasets/emisiones2018.csv", sep=";")
emisiones_2020 = pd.read_csv("../Datasets/emisiones2019.csv", sep=";")

# Concatenar en un único DataFrame
emisiones = pd.concat(
    [emisiones_2017, emisiones_2018, emisiones_2019, emisiones_2020],
    ignore_index=True
)

# Columnas de los días
cols_dias = [col for col in emisiones.columns if col.startswith("D")]

# Selección final de columnas
emisiones = emisiones[
    ["ESTACION", "MAGNITUD", "ANO", "MES"] + cols_dias
]

# Reestructurar el dataframe
emisiones = emisiones.melt(
    id_vars=["ESTACION", "MAGNITUD", "ANO", "MES"],
    value_vars=cols_dias,
    var_name="DIA",
    value_name="VALOR"
)

# Limpiar columna DIA (quitar la 'D')
emisiones["DIA"] = emisiones["DIA"].str.strip().str[1:]

# Crear columna FECHA
emisiones["FECHA"] = pd.to_datetime(
    emisiones["ANO"].astype(str) + "-" +
    emisiones["MES"].astype(str).str.zfill(2) + "-" +
    emisiones["DIA"],
    errors="coerce"
)

import numpy as np

# Eliminar fechas no válidas (NaT)
emisiones = emisiones[~np.isnat(emisiones["FECHA"])]

### COMPROBACIONES:
# Ver las primeras filas del DataFrame final
print(emisiones.head())

# Ver información general (tipos de datos y nulos)
print(emisiones.info())

# Ver algunas filas aleatorias
print(emisiones.sample(10))

# Ver el rango de fechas
print(emisiones["FECHA"].min(), emisiones["FECHA"].max())


### EJERCICIO 5

# Hay 2 formas, vamos a hacerla de las 2:
# Forma básica: "Se puede poner las que queramos, no tienen porque estar todas."
emisiones = emisiones[
    ['ESTACION', 'MAGNITUD', 'FECHA']
]

# Forma avanzada (más realista si hay muchas columnas, para que aparezcan todas.)
orden = ['ESTACION', 'MAGNITUD', 'FECHA']
resto = [c for c in emisiones.columns if c not in orden]

emisiones = emisiones[orden + resto]
print("--------------------------- EMISIONES --------------------------------")
print(emisiones)






