# -*- codin
import numpy as np
import matplotlib as plt

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

#matplotlib
x = [1,2,3,4]
y = [10,20,25,30]
plt.plot(x,y, marker='o')
plt.title("Ejemplo de gráfico")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
