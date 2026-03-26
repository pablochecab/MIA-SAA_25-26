# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:43:02 2026

@author: Mañana
"""

#%% Unidad 4 - Práctica 2
import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Carga y preprocesado
df_datos = pd.read_csv("advertising.csv")
df_estandarizado = pd.DataFrame(
    StandardScaler().fit_transform(df_datos[['Age', 'Area Income']]),
    columns=['Age', 'Area Income']
)

# PCA
pca = PCA()
df_rotado = pd.DataFrame(
    pca.fit_transform(df_estandarizado),
    columns=['Negro', 'Rojo']
)

valores = pca.explained_variance_
vectores = pca.components_
v1, v2 = vectores[:, 0], vectores[:, 1]

print('Matriz de covarianza: ', pca.get_covariance())
print('Valores propios: ', valores)
print(f"Valor 1: {valores[0]} Vector 1: {v1}")
print(f"Valor 2: {valores[1]} Vector 2: {v2}")

# Visualizacion de 4 subplots
fig, axes = pl.subplots(2,2,figsize=(8,8))

# Datos originales
ax = axes[0,0]
ax.set_title('Datos originales')
ax.set_label('Age')
ax.set_ylabel('Area Income')
ax.scatter(df_datos['Age'], df_datos['Area Income'], color='green')

# Datos estandarizados
ax = axes[0,1]
ax.set_title('Datos estandarizados')
ax.set_label('Age')
ax.set_ylabel('Area Income')
ax.scatter(df_estandarizado['Age'], df_estandarizado['Area Income'], color='blue')

# Datos estandarizados + vectores propios
ax = axes[1,0]
ax.set_title('Datos estandarizados con vectores propios')
ax.set_label('Age')
ax.set_ylabel('Area Income')
ax.scatter(df_estandarizado['Age'], df_estandarizado['Area Income'], color='red')
qargs = dict(scale = 1, scale_units='xy', angles='xy')
ax.quiver(0,0, v1[0] / abs(v1[0]) * valores[0], v1[1] / abs(v1[1]) * valores[0], color='black', **qargs)
ax.quiver(0,0, v2[0] / abs(v2[0]) * valores[1], v2[1] / abs(v2[1]) * valores[1], color='black', **qargs)

# Datos rotados y proyectados
ax = axes[1,1]
ax.set_title('Datos estandarizados, rotados y proyectados')
ax.set_xlabel('Negro')
ax.set_ylabel('Rojo')

ax.scatter(df_rotado['Negro'], df_rotado['Rojo'], color='grey')

# Proyecciones en ejes
ax.scatter(df_rotado['Negro'], np.full(len(df_rotado), df_rotado['Rojo'].min()), color='black')
ax.scatter(np.full(len(df_rotado), df_rotado['Negro'].min()), df_rotado['Rojo'], color='red')

pl.tight_layout()
pl.show()

# Nuevos datos
pl.figure()
pl.title('Nuevos Datos')

pl.scatter(df_rotado['Negro'], np.full(len(df_rotado), 1), color='black')
pl.scatter(df_rotado['Rojo'], np.full(len(df_rotado), 2), color='red')

pl.tight_layout()
pl.show()