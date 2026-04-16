import numpy as np
import pandas as pd

def tamaño_matriz():
    
    tamaño_matriz = []

    while True:
        try: 
            tamaño_matriz_i = int(input(f"Ingrese el tamaño de la matriz | FILA | i:"))  
            if tamaño_matriz_i >= 0:
                print(f"Numera de filas {tamaño_matriz_i}")
                break
            else:
                print("EL numero de filas debe ser mayor o igual a 0")       
        except ValueError:
            print("Entrada no valida")
        
    while True:
        try: 
            tamaño_matriz_j = int(input(f"Ingrese el tamaño de la matriz | COLUMNA | j:"))  
            if tamaño_matriz_j >= 0:
                print(f"Numera de columnas {tamaño_matriz_j}")
                break
            else:
                print("EL numero de columnas debe ser mayor o igual a 0")       
        except ValueError:
            print("Entrada no valida")        
                
    tamaño_matriz = tamaño_matriz_i, tamaño_matriz_j
    return tamaño_matriz

def crear_matriz(filas, columnas):
    print("\n")
    print("\n\t CREACION DE MATRIZ")
    matriz = np.zeros((filas, columnas))
    print (matriz)
    for i in range (filas):
        for j in range (columnas):
            valor = float(input(f"Ingrese valor en (i{i},j{j}): "))
            matriz[i][j] = valor
    print(matriz)
    return matriz        
    
def transformacion(matriz_figura):
    matriz_transformacion = np.zeros((2, 2))
    print("\n")
    print("\n\t CREACION DE MATRIZ DE TRANSFORMACION")
    print(matriz_transformacion)
    for i in range (2):
        for j in range (2):
            valor = float(input(f"Ingrese valor en (i{i},j{j}): "))
            matriz_transformacion[i][j] = valor
    matriz_resultante = matriz_transformacion @ matriz_figura 
    print(matriz_resultante)
    

i,j = tamaño_matriz()      
matriz = crear_matriz(i, j) 
transformacion(matriz)