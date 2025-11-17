# -*- codin
import numpy as np
import matplotlib.pyplot as plt

#%%Seccion inicial, arrays y randoms.
print ("A y B")
a = np.array([1,2,3,4])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a.shape)
print(b)
print(b.shape)
print ("ARANGE C")
c = np.arange(1.0 , 3.0 , 0.5)
print(c)

"""
El primer numero de zeros indica la cantidad de arrays
y el segundo la cantidad de ceros que queremos en cada uno.
"""
zerosArray = np.zeros((2,3))
print("Array de ceros:\n ", zerosArray)

onesArray = np.ones((3,2))
print("array de unos: \n", onesArray)

identidad = np.identity(4)
print("array identidad \n", identidad)

randomArray = np.random.random((2,3))
print("randomArray: \n", randomArray)

randomSample = np.random.ranf((4,3))
print("randomSample: \n", randomSample)

enterosRandom = np.random.randint(10,50,(3,3))
print("enterosRandom: \n", enterosRandom)

#%% Seccion operaciones matemáticas:
print("enterosRandom: \n")
x= np.array([[1,2],[3,4]])
y= np.array([[6,7],[8,9]])
print(x)
print(y)

print("\nsuma:\n", x+y)
print("\nresta:\n", x-y)
print("\nmultiplicacion:\n", x*y)
print("\nproducto escalar:\n", np.dot(x,y))
print("\ndivision:\n", x/y)


""" CTRL + ENTER ejecutar solo esa linea 
    Al poner clear se limpia la consola 
    Tambien sirve de calculadora
    CTRL + ALT + FLECHA, duplica linea de arriba"""
    
#@@ Ejercicios propuestos
# EJERCICIO 11

m_1 = np.array([4,9,4])                
m_2 = np.array([[8, 2, 7], [8, 2, 7]]) 
m_3 = np.zeros((3, 3))
print(m_1)
print(m_2)
print(m_3)

# EJERCICIO 12
ide = np.identity(5)
print(f" Array identidad: \n", ide)
randoms = np.random.randint(0,2,(3,3))
print(f" Array numeros aleatorios: \n", randoms)

# EJERCICIO 13
x = np.array([[1,2],[3,4]])
y = np.array([[6,7],[8,9]])
print(x)
print(y)

print("\nsuma:\n", x+y)
print("\nmultiplicacion:\n", x*y)

# EJERCICIO 14:
matriz_aleatoria = np.random.randint(0, 101, (5,5))
print("Matriz aleatoria 5x5:\n", matriz_aleatoria)

maximo = matriz_aleatoria.max()
print("Valor máximo:", maximo)

minimo = matriz_aleatoria.min()
print("Valor mínimo:", minimo)

media = matriz_aleatoria.mean()
print("Media:", media)

#%% matplotlib
x = [1,2,3,4]
y = [10,20,25,30]

plt.title("Ejemplo de gráfico")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.xlim(0,5)
plt.ylim(0,505)
#plt.show

fig, axs = plt.subplots(2,2, figsize=(8,4))
axs[0,0].plot(x,y, marker='o')
axs[0,0].set_title("linea")
axs[0,0].set_xlim(0,5)
axs[0,0].set_ylim(0,35)
axs[0,1].bar(x,y, color='orange')
axs[0,1].set_title("barras")
axs[1,0].scatter(x,y, color='red')
axs[1,0].set_title("dispersion")
axs[1,1].hist(y, color='purple')
axs[1,1].set_title("histograma")

x = [10,20,30,40,50]
y = [100, 200, 300, 400, 500]

#%% graficos seno coseno
x = np.arange(0, 10, 0.1)
# Calculamos dos funciones
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure(figsize=(8,5))  # tamaño del gráfico
# Dibujar las dos líneas (azul continua y roja discontinua)
plt.plot(x, y1, color='blue', linestyle='-', label='Seno')
plt.plot(x, y2, color='red', linestyle='--', label='Coseno')

#%% pandas
import pandas as pd
ruta = r"C:\Users\Mañana\Desktop\unsdg_2002_2021.csv"
df = pd.read_csv(ruta, sep=',')
print(df.head())
print("-----------------\n")
print(df.info())
print("-----------------\n")
print(df.describe())
print("-----------------\n")
print(df.columns.values)
print("-----------------\n")
print(df.index)
print(df.info())
print("-----------------\n")
print("ordenando valores de Las fechas")
print(df.sort_values("dt_year", ascending=True))
print("USANDO INFORMACIÓN: iloc[]")
print("USANDO ILOC PARA PRIMERA FILA")
print(df.iloc [1])
print("-----------------\n")
print("USANDO LOC[] PARA de_year")
# df_2020= df.loc[df["dt_year"]==2020]
# print(df_2020.head)
print(df.drop_duplicates())
print(df.drop_duplicates(subset='dt_year'))
print(df.dropna())
print("-----------------\n CORRIGIENDO NAN")
print(df.dropna(how='all'))
print(df.fillna(0))




#%%
import pandas as pd
data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee1", "Employee2", "Employee3"])
print(df)
print("-----------------\nEMPLEADO 2")
print(df.loc["Employee2"])
print(df.iloc[1])

#añadir columna
df["Job"] = ["cocinero", "nuevo", "cajero"]
print(df)
#añadir fila
nuevaFila = pd.DataFrame([{"Name":"Sandy", "Age":28,"Job":"Ingeniera"},
                         {"Name":"Cangrejo", "Age":60,"Job":"jefe"}], index=["Employee4","Employee5"])

df = pd.concat([df,nuevaFila])
print(df)

