import random

def bucket_sort(arr):
    # Verifica se o array está vazio
    if len(arr) == 0:
        return arr

    # Determina o número de buckets
    max_val = max(arr)
    num_buckets = max_val + 1

    # Cria buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribui os elementos nos buckets
    for num in arr:
        buckets[num].append(num)

    # Ordena cada bucket
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])

    # Combina os buckets ordenados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Programa principal
if __name__ == "__main__":
    n = int(input("Insira o número de elementos do array: "))
    maximo = n * 10
    data = [random.randint(1, maximo) for _ in range(n)]

    print("Vetor original:", data)
    sorted_data = bucket_sort(data[:])
    print("Array ordenado:", sorted_data)
