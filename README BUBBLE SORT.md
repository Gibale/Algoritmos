Lo que se hace iniciando el algoritmo Bubble Sort, se importa tiempo para tomar el tiempo que tarda el algoritmo en correr y random para poder desordenar valores de n.

import time
import random

Luego se define el algoritmo bubblesort con la variable L para que pueda trabajar con los valores dentro, se declara que n es igual a la longitud de los elementos de L.
Posteriormente se usa el comendo for para algún "i" en un rango de 0 hasta n.

def bubblesort(L):

    n = len(L)
    for i in range(0, n):

Dentro de este for, se dice para algún "j" en un rango de n-1, i, y -1,
Si algún elemento de L es mayor a algún elemento de L - 1, entonces key tendrá el valor de un elemento de L, ese elemento de L será igual a un elemento de L - 1 y L - 1 será igual a key.
Finalmente, se retorna L como valor a la función.

def bubblesort(L):

            for j in range(n - 1, i, -1):
            if L[j] < L[j - 1]:
                key = L[j]
                L[j] = L[j - 1]
                L[j - 1] = key
    return L
    
Al final del código, se define el valor de n y se meten en una lista de L, luego se desordenan los valores y se toma el tiempo inicial, se ejecuta la función, se toma tiempo final y se resta tiempo final - tiempo total para obtener el tiempo total y se imprimen.

n = 50000
L = list(range(n))
random.shuffle(L)

inicio = time.time()
bubblesort(L)
final = time.time()
total = final - inicio
print("El tiempo inicial es de: ", inicio)
print("El tiempo final es de: ", final)
print("El tiempo total es de: ", total)
