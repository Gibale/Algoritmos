import time
import random


def insertion_sort(A):

    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
        fin = time.time()
    return A


n = 10000
A = list(range(n))
random.shuffle(A)
inicio = time.time()
insertion_sort(A)
final = time.time()
print("Tiempo inicial: ", inicio)
print("Tiempo final: ", final)
print("Tiempo total: ", final - inicio)
