# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 08:48:08 2025

@author: Mañana
"""

import numpy as np

A = np.array([1,2,3,4])
B = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Print normal: ", A)
print("Print normal de B: ", B)
print("Shape de A: ", np.shape(A))
print("Shape de B: ", np.shape(B))
print("-------------------------------------------")
zeros_array = np.zeros((2, 3))  # a) Array de ceros
print("\nArray de ceros (2x3):\n", zeros_array)

ones_array = np.ones((3, 2))  # b) Array de unos
print("\nArray de unos (3x2):\n", ones_array)

identidad = np.identity(4)  # c) Array identidad
print("\nMatriz identidad (4x4):\n", identidad)

random_array = np.random.random((2, 3))  # valores aleatorios entre 0 y 1
print("\nArray aleatorio random():\n", random_array)

random_sample = np.random.ranf((2, 2))  # random_sample() / ranf()
print("\nArray aleatorio ranf():\n", random_sample)

enteros_random = np.random.randint(10, 50, (3, 3))  # enteros aleatorios entre 10 y 50
print("\nArray de enteros aleatorios randint():\n", enteros_random)
