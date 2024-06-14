import random


def selection_sort(arr):
    n = len(arr)
    iterations = 0

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            iterations += 1

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr, iterations


# Peça ao usuário para escolher o número de posições do array
n_posicoes = int(input("Insira o número de posições do array: "))

max = n_posicoes * 10
# Crie um array de exemplo com o número de posições escolhido
arr = [random.randint(1, max) for _ in range(n_posicoes)]

print("Array original:")
for num in arr:
    print(num, end=' ')
print("\nArray ordenado:")
arr_ordenado, num_iteracoes = selection_sort(arr)
for num in arr_ordenado:
    print(num, end=' ')
print(f"\n\nNúmero de iterações: {num_iteracoes}")
