def quick_sort(arr):
    iterations = 0
    stack = [(0, len(arr) - 1)]
    
    while stack:
        iterations += 1
        low, high = stack.pop()
        
        if low < high:
            pivot = arr[(low + high) // 2]
            i = low - 1
            j = high + 1
            
            while True:
                i += 1
                while arr[i] < pivot:
                    i += 1
                
                j -= 1
                while arr[j] > pivot:
                    j -= 1
                
                if i >= j:
                    break
                
                arr[i], arr[j] = arr[j], arr[i]
            
            stack.append((low, j))
            stack.append((j + 1, high))
    
    return arr, iterations

# Exemplo de uso:
import random

# Peça ao usuário para escolher o número de posições do array
n_posicoes = int(input("Insira o número de posições do array: "))

max = n_posicoes * 10
# Crie um array de exemplo com o número de posições escolhido
arr = [random.randint(1, max) for _ in range(n_posicoes)]

print("Vetor original:", arr)

# Ordena o vetor com QuickSort
arr, iterations = quick_sort(arr)
print("Vetor ordenado:", arr)
print("Número de iterações:", iterations)
