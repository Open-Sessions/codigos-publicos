import numpy as np
import random


def generar_matriz(n):
    matriz = np.empty((n,n))

    for i in range(n):
        for j in range(n):
            matriz[i][j]= random.randrange(1,(n+n))
    print(matriz)
    return matriz


def recorrer_caracol_nuevo(matriz):
    num_ciclo=0
    cuenta =1
    mitad = (n-1)//2
    print(mitad)
    fila_actual=mitad
    columna_actual = mitad
    total_elementos=n*n
    vectorResultado = []
    while cuenta<(total_elementos):
        #derecha, arriba
        derechaDir =True
        arribaDir = False
        num_ciclo =num_ciclo+1
        while (derechaDir or arribaDir):
            #ciclos derecha
            derecha=0
            while(derecha<num_ciclo):
                vectorResultado.append(matriz[fila_actual][columna_actual])
                print(matriz[fila_actual][columna_actual])
                columna_actual =columna_actual+1
                if columna_actual == n:
                    columna_actual = n-1
                    derecha+=1
                cuenta =cuenta+1
                if cuenta > total_elementos:
                    return vectorResultado
                derechaDir=False
                arribaDir=True
                derecha+=1
                    #ciclos derecha
            arriba=0
            while(arriba<num_ciclo):
                vectorResultado.append(matriz[fila_actual][columna_actual])
                print(matriz[fila_actual][columna_actual])
                fila_actual =fila_actual-1
                if fila_actual == -1:
                    fila_actual = 0
                cuenta =cuenta+1
                if cuenta > total_elementos:
                    
                    return vectorResultado
                derechaDir=False
                arribaDir=False
                arriba+=1
        #izquierda, abajo

        num_ciclo = num_ciclo+1
        izquierdaDir=True
        abajoDir=False
        while (izquierdaDir or abajoDir):
            #ciclos izquierda
            izquierda=0
            while(izquierda<num_ciclo):
                vectorResultado.append(matriz[fila_actual][columna_actual])
                print(matriz[fila_actual][columna_actual])
                columna_actual =columna_actual-1
                if columna_actual == -1:
                    columna_actual = 0
                cuenta =cuenta+1
                if cuenta > total_elementos:
                    return vectorResultado
                izquierdaDir=False
                abajoDir=True
                izquierda+=1
            #ciclos abajo
            abajo=0
            while(abajo<num_ciclo):
            
                vectorResultado.append(matriz[fila_actual][columna_actual])
                print(matriz[fila_actual][columna_actual])
                fila_actual =fila_actual+1
                if fila_actual == n:
                    fila_actual = n-1
                cuenta =cuenta+1
                izquierdaDir=False
                abajoDir=False
                abajo+=1
                if cuenta > total_elementos:
                    return vectorResultado


def recorrer_caracol(matriz):
    #Arreglo para almacenar valores del recorrido
    valores = []
    #Punto de partida
    mitad = (n-1)//2
    print(mitad)
    valores.append(matriz[mitad][mitad])
    #Variables auxiliares para almacenar información
    nueva_fila = mitad
    nuevo_columna = mitad
    contador = 0
    total_elementos = n*n
    derecha = True
    izquierda = False
    abajo = False
    arriba = False

    #empieza el recorrido
    for k in range(total_elementos-1):
        if derecha:
            nuevo_columna = nuevo_columna + 1
            if nuevo_columna == n:
                nuevo_columna= n-1
                nueva_fila = nueva_fila -1
                derecha = False
                arriba = True
        elif arriba:
            nueva_fila = nueva_fila -1
            if nueva_fila == -1:
                nueva_fila = 0
                nuevo_columna = nuevo_columna -1
                arriba = False
                izquierda = True
        elif izquierda:
            nuevo_columna = nuevo_columna -1
            if nuevo_columna == -1:
                nuevo_columna = 0
                nueva_fila = nueva_fila + 1
                izquierda = False
                abajo = True
        else:
            nueva_fila = nueva_fila + 1
            if nueva_fila == n:
                nueva_fila = n-1
                nuevo_columna = nuevo_columna + 1
                abajo = False
                derecha = True
        valores.append(matriz[nueva_fila][nuevo_columna])
    
    print(valores)
    return valores


def formar_columna(nro,arreglo):
    numeros_menores = 0
    numeros_mayores = 0
    numeros_iguales = 0
    columna = []
    for elemento in arreglo:
        if int(elemento)<nro:
            numeros_menores+=1
        elif int(elemento)>nro:
            numeros_mayores+=1
        else:
            numeros_iguales+=1
    columna.append(numeros_menores)
    columna.append(numeros_mayores)
    columna.append(numeros_iguales)

    return columna
    






n = int(input("Ingrese el número de dimensiones: "))

if n%2!=0:
    print("El número ingresado está OK")
    matriz = generar_matriz(n)
    arreglo = recorrer_caracol_nuevo(matriz)
    nro_a = int(arreglo[(len(arreglo)-1)])
    nro_b = arreglo[nro_a]
   
    columna1 = formar_columna(nro_b,arreglo)
    columna2 = formar_columna(nro_a,arreglo)
    matriz_resultante = np.array([columna1,columna2])
    matriz_resultante_transpuesta = np.transpose(matriz_resultante)

    
    print(matriz_resultante_transpuesta)

else:
    print("El número está incorrecto")



