import random


def insertion_sort(arr):
    n = len(arr)
    iterations = 0

    for i in range(1, n):
        key = arr[i]
        j = i-1
        iterations += 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            iterations += 1

        arr[j+1] = key

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
arr_ordenado, num_iteracoes = insertion_sort(arr)
for num in arr_ordenado:
    print(num, end=' ')
print(f"\n\nNúmero de iterações: {num_iteracoes}")
