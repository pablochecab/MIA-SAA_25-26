# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 11:13:52 2025

@author: Mañana
"""

import pandas as pd
import random

dfDatos = pd.DataFrame()

# --------------------------------------------------------
# 1) Cargar datos y crear dos columnas categóricas nuevas
# --------------------------------------------------------

def cargarDatos():
    
    dfDatos = pd.read_csv("Datasets/Walmart_Sales.csv")

    return dfDatos


# --------------------------------------------------------
# 2) insertarColumnas: añade columnas SOLO a Store == 2
# --------------------------------------------------------

def insertarColumnas(dfDatos):

    # Nuevas categorías
    valoresCustomerFlow = ["Bajo", "Medio", "Alto", "Muy_Alto"]    # 4 valores
    valoresDayType = ["Laboral", "Festivo"]                        # 2 valores

    # Listas "Columnas" donde se guardarán los valores generados
    customer_Flow = []
    day_Type = []

    # Añadir los valores con bucles
    for i in range(dfDatos.shape[0]):
        customer_Flow.append(valoresCustomerFlow[random.randint(0, 3)])
        day_Type.append(valoresDayType[random.randint(0, 1)])

    # Insertamos las columnas "titulos también" en el DataFrame
    dfDatos["Customer_Flow"] = customer_Flow
    dfDatos["Day_Type"] = day_Type

    # Filtrar solo store 2
    dfDatos = dfDatos[dfDatos["Store"] == 2]

    return dfDatos


dfDatos = cargarDatos()
dfDatos = insertarColumnas(dfDatos)

print("\n\nDataFrame (Store 2)")
print(dfDatos)

print("\n\nVer si hay algún null:")
print(dfDatos.isnull())

print("\n\nSuma de nulls:")
print(dfDatos.isnull().sum())
