Algoritmo Insertion Sort:
Al inicio del algoritmo insertion sort lo que hago al inicio es importar la librería de tiempo "time" para que pueda tomar el tiempo que tarda el algoritmo en terminar y la librería "random" para poder sacar desordenar cada uno de los valores de n.

_import time
_import random

Luego se procede a definir la función insertion_sort con la variable A para que esta pueda trabajar sobre los valores de n en una lista.
En la siguiente línea se ejecuta el código de tal manera que busque algún valor en el rango y longitud de la lista A, key será igual a algún valor dentro de A e "i" será igual a j - 1.

_def insertion_sort(A):

    for j in range(len(A)):
        key = A[j]
        i = j - 1

Dentro del for, mientras "i" sea mayor o igual a 0 y key sea menor a algún número de A, se tomará algún número de A + 1 y será igual a algún otro número de A, e "i" será igual a i - 1.

        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i = i - 1

Luego algún valor dentro de A + 1 será igual a key y se irá retornando A
Al final del código se define el valor de n y luego se ponen en una lista "A" para que se pueda iterar entre cada uno de los valores, para hallar el tiempo total que toma el algoritmo para ejecutarse, se resta el tiempo inicial menos el tiempo final.

_return A


_n = 10000
A = list(range(n))
random.shuffle(A)
inicio = time.time()
insertion_sort(A)
final = time.time()
print("Tiempo inicial: ", inicio)
print("Tiempo final: ", final)
print("Tiempo total: ", final - inicio)
