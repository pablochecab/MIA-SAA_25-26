# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 10:38:32 2026

@author: Mañana
"""

### a) Importar librerías necesarias
import pandas as pd  # Para manipulación de datos en DataFrames
from sklearn.datasets import fetch_california_housing  # Para cargar el dataset California Housing
from sklearn.model_selection import train_test_split  # Para dividir datos en entrenamiento y prueba
from sklearn.linear_model import LinearRegression  # Para crear el modelo de regresión lineal
from sklearn.metrics import mean_squared_error, r2_score  # Para evaluar el desempeño del modelo
from sklearn.preprocessing import StandardScaler  # Para normalizar/estandarizar los datos

### b) Cargar el dataset California Housing
california = fetch_california_housing()  

### c) Crear un DataFrame con las variables predictoras y añadir la variable objetivo PRICE
df = pd.DataFrame(california.data, columns=california.feature_names)   # Creamos un DataFrame con las columnas originales del dataset
df['PRICE'] = california.target   # Añadimos la columna 'PRICE', que será la variable que queremos predecir

### d) Crear un array 'caracteristicas' con las variables independientes
caracteristicas = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 
                   'Population', 'AveOccup', 'Latitude', 'Longitude']
# Estas son las 8 características que vamos a usar para predecir el precio

### e) Separar variables predictoras (X) y variable objetivo (y)
X = df[caracteristicas]  # DataFrame con solo las columnas que usaremos como entrada
y = df['PRICE']           # Vector con los precios (variable objetivo)

### f) Dividir los datos en conjunto de entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# test_size=0.2 → 20% de los datos se usarán para prueba
# random_state=42 → asegura que la división sea reproducible

# Mostrar dimensiones para verificar
print("Dimensiones de X_train:", X_train.shape)  # Filas y columnas del conjunto de entrenamiento
print("Dimensiones de X_test:", X_test.shape)    # Filas y columnas del conjunto de prueba
print("Dimensiones de y_train:", y_train.shape)  # Número de valores objetivos para entrenamiento
print("Dimensiones de y_test:", y_test.shape)    # Número de valores objetivos para prueba

### g) Aplicar normalización (escalado) de los datos usando StandardScaler
scaler = StandardScaler()  # Creamos una instancia de StandardScaler

# Ajustamos el escalador solo con los datos de entrenamiento
scaler.fit(X_train)

# Transformamos los datos de entrenamiento y de prueba
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Ahora X_train_scaled y X_test_scaled tienen medias cercanas a 0 y desviación estándar de 1
# Esto ayuda a que el modelo lineal funcione mejor y evite problemas por escalas diferentes de las variables

### h) Crear el modelo de regresión lineal y entrenarlo
modelo = LinearRegression()  # Creamos la instancia del modelo
modelo.fit(X_train_scaled, y_train)  # Entrenamos el modelo con los datos escalados de entrenamiento

### i) Realizar predicciones sobre el conjunto de prueba
prediccionConjuntoPrueba = modelo.predict(X_test_scaled)  
# .predict() devuelve un array con los precios predichos para X_test_scaled

### j) Calcular el Error Cuadrático Medio (MSE)
mse = mean_squared_error(y_test, prediccionConjuntoPrueba)
print("Error Cuadrático Medio (MSE):", mse)
# MSE mide el promedio de los errores al cuadrado entre los precios reales y predichos
# Mientras más pequeño sea, mejor predice el modelo

### k) Calcular el Coeficiente de Determinación (R²)
r2 = r2_score(y_test, prediccionConjuntoPrueba)
print("Coeficiente de Determinación (R²):", r2)
# R² indica qué proporción de la variación del precio es explicada por el modelo
# Valor cercano a 1 → modelo explica muy bien los datos
# Valor cercano a 0 → modelo explica poco

### l) Mostrar los coeficientes del modelo para cada variable
print("Coeficientes del modelo:")
for nombre, coef in zip(caracteristicas, modelo.coef_):
    print(f"{nombre}: {coef}")
# modelo.coef_ devuelve un array con los pesos asignados a cada variable
# Esto nos permite ver qué variables tienen mayor impacto en el precio

