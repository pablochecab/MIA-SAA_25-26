# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 10:57:59 2026

@author: Mañana
"""

# ==========================================================
# REGRESIÓN LOGÍSTICA CON VALIDACIÓN CRUZADA (5-FOLD)
# Dataset: Iris
# Variables utilizadas: sepal length y sepal width
# ==========================================================

# ----------------------------------------------------------
# a) Importación de librerías
# ----------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


# ----------------------------------------------------------
# b) Cargar el dataset Iris
# ----------------------------------------------------------
# load_iris() devuelve un diccionario con:
# - data: variables predictoras
# - target: etiquetas (0,1,2)
# - feature_names: nombres de columnas
datosIris = load_iris()


# ----------------------------------------------------------
# c) Crear un DataFrame con las variables y el target
# ----------------------------------------------------------
# Creamos el DataFrame con las variables predictoras
dfIris = pd.DataFrame(datosIris.data, columns=datosIris.feature_names)

# Añadimos la columna objetivo (target)
dfIris['target'] = datosIris.target


# ----------------------------------------------------------
# d) Seleccionar las características (variables independientes)
# ----------------------------------------------------------
# Solo usaremos largo y ancho del sépalo
caracteristicas = ['sepal length (cm)', 'sepal width (cm)']


# ----------------------------------------------------------
# e) Separar variables predictoras (X) y variable objetivo (y)
# Target es un array que contiene valores de 0 a 2, siendo cada uno un iris distinto
# ----------------------------------------------------------
X = dfIris[caracteristicas]   # Variables independientes
y = dfIris['target']          # Variable dependiente


# ----------------------------------------------------------
# f) Normalización de los datos
# ----------------------------------------------------------
# La Regresión Logística funciona mejor si las variables
# están escaladas (media=0, desviación=1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# ----------------------------------------------------------
# g) Crear el modelo de Regresión Logística
# ----------------------------------------------------------
modelo = LogisticRegression()


# ----------------------------------------------------------
# h) Validación cruzada con 5 pliegues
# ----------------------------------------------------------
cv_accuracy = cross_val_score(modelo, X_scaled, y, cv=5, scoring='accuracy')

print("Precisión en cada pliegue:")
print(cv_accuracy)

print("\nPrecisión media:")
print(np.mean(cv_accuracy))


# ----------------------------------------------------------
# i) Entrenar el modelo con todos los datos
# ----------------------------------------------------------
modelo.fit(X_scaled, y)


# ----------------------------------------------------------
# j) Cálculo de la frontera de decisión
# ----------------------------------------------------------

# Obtener valores mínimos y máximos de cada característica
x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1

# Crear la malla de puntos
xx, yy = np.meshgrid(
    np.arange(x_min, x_max, 0.02),
    np.arange(y_min, y_max, 0.02)
)

# Predecir las clases sobre la malla
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)


# ----------------------------------------------------------
# k) Representación gráfica
# ----------------------------------------------------------

plt.figure(figsize=(8, 6))

# Superficie de decisión
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Set1)

# Puntos reales del dataset
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=y,
    edgecolor='k',
    cmap=plt.cm.Set1
)

plt.xlabel('Sepal length (scaled)')
plt.ylabel('Sepal width (scaled)')
plt.title('Regresión Logística con Validación Cruzada (Iris)')

plt.show()