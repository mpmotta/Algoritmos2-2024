def heapify(arr, n, i, iterations):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
        iterations += 1
    
    if right < n and arr[right] > arr[largest]:
        largest = right
        iterations += 1
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        iterations += 1
        return arr, iterations
    
    return arr, iterations

def heap_sort(arr):
    n = len(arr)
    iterations = 0
    
    for i in range(n // 2 - 1, -1, -1):
        arr, iterations = heapify(arr, n, i, iterations)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arr, iterations = heapify(arr, i, 0, iterations)
    
    return arr, iterations

# Exemplo de uso:
import random

# Peça ao usuário para escolher o número de posições do array
n_posicoes = int(input("Insira o número de posições do array: "))

max = n_posicoes * 10
# Crie um array de exemplo com o número de posições escolhido
arr = [random.randint(1, max) for _ in range(n_posicoes)]

print("Vetor original:", arr)

# Ordena o vetor com Heap Sort
arr, iterations = heap_sort(arr)
print("Vetor ordenado:", arr)
print("Número de iterações:", iterations)
