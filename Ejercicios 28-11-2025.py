# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 10:53:25 2025

@author: Mañana
"""

# 1. Cargar el conjunto de datos breast_cancer y pasarlo a DataFrame
from sklearn.datasets import load_breast_cancer
import pandas as pd

# Cargar dataset
cancer = load_breast_cancer()

# Crear DataFrame usando los nombres de las características como columnas
df = pd.DataFrame(cancer.data, columns=cancer.feature_names)

# Mostrar las 5 primeras filas
print("Primeras 5 filas del DataFrame original:")
print(df.head())


# 2. Sustituir todos los valores 0.0 por el valor más frecuente usando SimpleImputer
from sklearn.impute import SimpleImputer
import numpy as np

# Crear el imputador con estrategia 'most_frequent'
imputer = SimpleImputer(missing_values=0.0, strategy='most_frequent')

# Aplicarlo sobre los datos
dfImputado = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Mostrar el DataFrame imputado
print("\nDataFrame imputado (0.0 reemplazados por el valor más frecuente):")
print(dfImputado)


# 3. Crear dfCancerModificado eliminando 'worst symmetry' y ordenando por 'mean texture'
dfCancerModificado = dfImputado.copy()

# Eliminar la columna 'worst symmetry'
dfCancerModificado.drop(columns=['worst symmetry'], inplace=True)

# Ordenar por 'mean texture' de forma ascendente
dfCancerModificado.sort_values(by='mean texture', ascending=True, inplace=True)

# Mostrar el DataFrame resultante
print("\nDataFrame modificado:")
print(dfCancerModificado)
