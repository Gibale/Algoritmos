import time
import random


def bubblesort(L):

    n = len(L)
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if L[j] < L[j - 1]:
                key = L[j]
                L[j] = L[j - 1]
                L[j - 1] = key
    return L


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
