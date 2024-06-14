import random


def count_sort(arr):
    # Encontrar o tamanho máximo do vetor
    max_value = max(arr)

    # Criar um vetor de contadores com tamanho igual ao tamanho máximo
    count = [0] * (max_value + 1)

    # Contar a ocorrência de cada valor no vetor
    for num in arr:
        count[num - 1] += 1

    # Construir o vetor ordenado
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + 1] * count[i])

    return sorted_arr


# Solicitar o número de posições do vetor
n = int(input("Digite o número de posições do vetor: "))

# Gerar valores aleatórios para o vetor (só números positivos)
max_value = n * 10
arr = [random.randint(1, max_value) for _ in range(n)]

# Exibir o vetor original
print("Vetor original:", arr)

# Ordenar o vetor
sorted_arr = count_sort(arr)

# Exibir o vetor ordenado
print("Vetor ordenado:", sorted_arr)
