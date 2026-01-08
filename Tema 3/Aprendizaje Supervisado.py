# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 10:46:47 2026

@author: Mañana
"""

### Ejercicios repaso-ampliacion 1

import pandas as pd

"""
def cotizaciones(fichero):
    # Leer el archivo
    df = pd.read_csv(fichero, sep=';', thousands='.', decimal=',')

    # Eliminar columna nombre
    df = df.drop(columns=['Nombre'])

    # calcular el min, MAX, media
    # dataframe usando clave-valor pd.DataFrame({'col1': serie1, 'col2': serie2})
    resultado = pd.DataFrame({
        'Minimo': df.min(),
        'Maximo': df.max(),
        'Media': df.mean()
    })

    return resultado

fichero = '../Datasets/cotizacion.csv'
print(cotizaciones(fichero))  # llamamos a la funcion

"""

# HAY QUE VER PORQUE ESTE NO LO HACE BIEN Y EL DE ARRIBA SI

"""# a) Crear la función cotizaciones
def cotizaciones():
    # b) Leer el fichero indicando separador, miles y decimal:
    df = pd.read_csv('../Datasets/cotizacion.csv',
        sep=';',
        thousands='.',
        decimal=','
    )
    
    #print(df)
    
    # c) Eliminar la columna 'Nombre'
    df = df.drop(columns=['Nombre'])
    
    # d) Crear DataFrame usando formato clave:valor
    df_cotizaciones = pd.DataFrame({
        'Mínimo': df['Mínimo'],
        'Máximo': df['Máximo'],
        'Final': df['Final'] # Lo que se refiere el enunciado a "media" es final. Vamos a renombrarlo
    })
    
    # EXTRA: Renombrar la columna en el dataframe NUEVO.
    df_cotizaciones = df_cotizaciones.rename(columns={"Final": "Media"})
    
    # e) Retornar el DataFrame creado
    return df_cotizaciones


# Llamada a la función e impresión desde fuera
print(cotizaciones()) """


### Ejercicios repaso-ampliacion 1 (Apartado 2, TITANIC)

fichero2 = '../Datasets/titanic.csv'

def titanic(fichero2):
    
    # Leer el archivo
    df = pd.read_csv(fichero2, sep=',', thousands='.', decimal=',')
    
    # b) Imprimir dimensiones, tamaño, índice y las 10 últimas líneas
    print("Dimensiones (filas, columnas):", df.shape)
    print("Tamaño total (número de elementos):", df.size)
    print("Índice del dataframe:")
    print(df.index)
    print("\nÚltimas 10 filas del dataframe:")
    print(df.tail(10))

    # c) Datos del pasajero con identificador 148 usando loc[]
    # Ojo: indexación desde cero → PassengerId 148 corresponde al índice 147
    print("\nDatos del pasajero con identificador 148:")
    print(df.loc[147])

    # d) Mostrar por pantalla las filas pares usando iloc[range(...)]
    print("\nFilas pares del dataframe:")
    print(df.iloc[range(0, len(df), 2)])
    
    # e) Nombres de personas de primera clase (Pclass == 1) ordenadas alfabéticamente
    print("\nNombres de pasajeros de primera clase ordenados alfabéticamente:")
    print(df[df["Pclass"] == 1]["Name"].sort_values())
    
    return df

print(titanic(fichero2))

