import pandas as pd
import random

dfDatos = pd.DataFrame()

def cargarDatos():
    dfDatos = pd.read_csv("Datasets/Walmart_Sales.csv")
    valoresPosiblesWeeklyRain =["Ninguna","Pocas","Medias","Muchas"]
    weekly_Rains= []
    for i in range(dfDatos.shape[0]):
        weekly_Rains.append(valoresPosiblesWeeklyRain[random.randint(0,3)])

    dfDatos['Weekly_Rains'] = weekly_Rains

    valoresPosiblesWeeklyDiscounts = ["Carnes","Pescados","Restos"]
    weekly_Discounts = []
    for i in range(dfDatos.shape[0]):
        weekly_Discounts.append(valoresPosiblesWeeklyDiscounts[random.randint(0,2)])

    dfDatos["Weekly_Discounts"] = weekly_Discounts

    dfDatos = dfDatos[dfDatos.Store == 1]
    return dfDatos

dfDatos = cargarDatos()

# Los prints están hechos así por algún motivo.
print(dfDatos.shape[0])
print("\n\nTipo de datos:")
print(type(dfDatos))
print("\n\nDataframe dfDatos----------:\n")
print(dfDatos)
print("\n\nVer si hay algun null----------:\n")
print(dfDatos.isnull())
print("\n\nLa suma de cuantos null hay----------:\n")
print(dfDatos.isnull().sum())


### 05/12/2025

dfDatos = dfDatos.dropna(subset=['Store','Date','Weekly_Sales'])
dfDatos = dfDatos.reset_index(drop=True)
print("\n\nDataframe dfDatos tras usar dropna")
print(dfDatos)

# Imputaciones
dfDatos['Holiday_Flag'] = dfDatos['Holiday_Flag'].fillna(0)
media_temp = dfDatos['Temperature'].mean()
dfDatos['Temperature'] = dfDatos['Temperature'].fillna(media_temp)
mediana_fuel = dfDatos['Fuel_Price'].median()
dfDatos['Fuel_Price'] = dfDatos['Fuel_Price'].fillna(mediana_fuel)

moda_cpi = dfDatos['CPI'].mode()[0]
dfDatos['CPI'] = dfDatos['CPI'].fillna(moda_cpi)
ql_unemployment = dfDatos['Unemployment'].quantile(0.25)
dfDatos['Unemployment'] = dfDatos['Unemployment'].fillna(ql_unemployment)

print("\nNulos tras imputación")
print(dfDatos.isnull().sum())
print(moda_cpi)
print(mediana_fuel)
print(media_temp)

#Train_test split

from sklearn.model_selection import train_test_split
df_X = pd.DataFrame(dfDatos, columns=[
        'Store', 'Date', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI',
        'Unemployment', 'Weekly_Rains', 'Weekly_Discounts'])

df_Y = pd.DataFrame(dfDatos, columns=['Weekly_Sales'])

df_X_train, df_X_test, df_Y_train, df_Y_test = train_test_split(
        df_X, df_Y, test_size=0.2, random_state=100)
print("\nCantidad de filas y columnas de X:", df_X.shape)
print("\nCantidad de filas y columnas de Y:", df_Y.shape)
print("\nCantidad de filas y columnas de X_train:", df_X_train.shape)
print("\nCantidad de filas y columnas de X_test:", df_X_test.shape)
print("\nCantidad de filas y columnas de Y:", df_Y.shape)
print("\nCantidad de filas y columnas de Y_train:", df_Y_train.shape)
print("\nCantidad de filas y columnas de Y_test:", df_Y_test.shape)
print("\nDataFrame df_Y:", df_Y)
print("\nDataFrame df_X_train:", df_X_train)
print("\nDataFrame df_Y_train:", df_Y_train)
print("\nDataFrame df_X_test:", df_X_test)

print("//////////////////////////////////////////////////////////////////////////////")

from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# cargamos df original
df_datos = cargarDatos()

# creamos el objeto OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)

# transformamos columna categórica
matriz_onehot = encoder.fit_transform(df_datos[['Weekly_Discounts']])

# obtenemos nombres reales de columnas
arr_nombre_nuevas_columnas = encoder.get_feature_names_out(['Weekly_Discounts'])

# convertimos a DataFrame
df_nuevas_columnas_onehot = pd.DataFrame(
    matriz_onehot,
    columns=arr_nombre_nuevas_columnas,
    index=df_datos.index
)

# unimos al original
df_datos = df_datos.join(df_nuevas_columnas_onehot)

print("\n<df_datos OneHotEncoder>:")
print(df_datos.head())



# Normalizar con MinMaxScaler (escalado entre 0 y 1)
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

df_datos = cargarDatos()

# seleccionamos solo columnas numéricas a normalizar
columnas_a_normalizar = ['Fuel_Price', 'CPI']

# creamos el escalador y lo ajustamos + transformamos
minmax_scaler = MinMaxScaler()
df_normalizado = minmax_scaler.fit_transform(df_datos[columnas_a_normalizar])

# convertimos de nuevo a DataFrame
df_normalizado = pd.DataFrame(
    df_normalizado,
    columns = ['Fuel_Price_normaliz', 'CPI_normaliz'],
    index = df_datos.index
)

print("\nMínimo de Fuel_Price normalizado:", df_normalizado['Fuel_Price_normaliz'].min())
print("Máximo de CPI normalizado:", df_normalizado['CPI_normaliz'].max())


# añadimos las columnas al df original
df_datos = df_datos.join(df_normalizado)

df_datos[['Fuel_Price', 'Fuel_Price_normaliz']].hist(bins=30)
df_datos[['CPI', 'CPI_normaliz']].hist(bins=30)

plt.show()

from sklearn.preprocessing import StandardScaler
#media = 0 y desviacion tipica 1
scaler_std = StandardScaler()

#fit calcula media y desv tipica - transform aplica estandarizacion
arr_estandarizado = scaler_std.fit_transform(df_datos[['Fuel_Price', 'CPI']])
df_estandarizado = pd.DataFrame(
    arr_estandarizado,
    columns = ['Fuel_Price_std', 'CPI_std'],
    index=df_datos.index
)

print("MEDIA Fuel_Price estandarizado\n", df_estandarizado['Fuel_Price_std'].mean())
print("Desviaciómn Típica fuel price \n", df_estandarizado['Fuel_Price_std'].std())



