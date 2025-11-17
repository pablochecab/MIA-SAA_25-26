# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 11:09:09 2025

@author: Mañana
"""

import matplotlib.pyplot as plt

#@@Ejercicio 15

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

#Declaramos la grafica
plt.plot(x, y, marker='_', color='blue')
plt.title("Ejercicio 15")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()

#@@Ejercicio 16
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
ventas = [1000, 1523, 1100, 1245, 1654, 1632]

#Declaramos la gráfica
plt.plot(meses, ventas, marker='*', color='pink')
plt.title("Informe gráfico de ventas")
plt.xlabel("Meses")
plt.ylabel("Ventas realizadas")
plt.xlim(0, 2)
plt.ylim(1000, 2000)

#@@Ejercicio 17
fig, axs = plt.subplots(1,2, figsize=(8,3))

axs[0].set_title("Gráfica 1")
axs[1].set_title("Gráfica 2")


