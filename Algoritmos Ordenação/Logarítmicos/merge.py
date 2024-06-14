import random


def merge_sort(arr):
    n = len(arr)
    iterations = 0

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        left, left_iterations = merge_sort(left)
        right, right_iterations = merge_sort(right)

        iterations += left_iterations + right_iterations

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            iterations += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            iterations += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            iterations += 1

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
arr_ordenado, num_iteracoes = merge_sort(arr)
for num in arr_ordenado:
    print(num, end=' ')
print(f"\n\nNúmero de iterações: {num_iteracoes}")
