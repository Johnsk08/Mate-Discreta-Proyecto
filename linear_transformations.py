import numpy as np
import matplotlib.pyplot as ptl
def tamaño_matriz():
    
    tamaño_matriz = []
    tamaño_matriz_i = 2 #SIEMPRE pero siempre es 2 porq asi seran las filas , por los pares ordenados (x,y) 
                        #(1 0)                                                                               
                        #(0 1) esto serian los puntos (1,0) y (0,1) por eso no pueden existir mas filas.     

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
            
            while True:
                try:
                    valor = float(input(f"Ingrese valor en (i{i},j{j}): "))
                    
                    if valor >= 0:
                        matriz[i][j] = valor
                        break
                    
                    else:
                        print("El valor debe ser mayor o igual a 0")
                    
                except ValueError:
                    print("Entrada no valida")
    print(matriz)
    return matriz        
    
def transformacion(matriz_figura):
    matriz_transformacion = np.zeros((2, 2))
    print("\n")
    print("\n\t CREACION DE MATRIZ DE TRANSFORMACION")
    print(matriz_transformacion)
    
    for i in range (2):
        for j in range (2):
            while True:
                try:
                    valor = float(input(f"Ingrese valor en (i{i},j{j}): "))
                    
                    if valor >= 0:
                        matriz_transformacion[i][j] = valor
                        break
                    
                    else:
                        print("El valor debe ser mayor o igual a 0")
                        
                except ValueError:
                    print("Entrada no valida")
    matriz_resultante = matriz_transformacion @ matriz_figura 
    print(matriz_resultante)
    return matriz_resultante
    

def graficar(matriz, titulo):
    ptl.figure() 
    # matriz[0, :] este seria todo el eje x
    # matriz[1, :] este otro todo el eje y
    print("\nMostrando figura original...")
    ptl.plot(matriz[0, :] , matriz[1, :],  marker = 'o', linestyle="-", color = 'r')
    # matriz con los dos ultimos ejes para cerrar figura
    ptl.plot((matriz[0, 0], matriz[0, -1]), (matriz[1, 0], matriz[1, -1]), marker = 'o', linestyle="-", color = 'r')
    
    ptl.title(f"GRAFICO {titulo}")
    ptl.xlabel("Eje X")
    ptl.ylabel("Eje y")
    ptl.grid(True)
    ptl.show()
        
i,j = tamaño_matriz()      
matriz = crear_matriz(i, j) 
graficar(matriz, "ORIGINAL")
matriz_resultante = transformacion(matriz)
graficar(matriz_resultante, "TRANSFORMADO")