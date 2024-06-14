import random

# Radix sort em Python


# Usando counting sort para ordenar os elementos com base nas posições significativas
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calcula a contagem de elementos
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calcula a contagem cumulativa
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Coloca os elementos em ordem
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Função principal para implementar o radix sort
def radixSort(array):
    # Obtém o elemento máximo
    max_element = max(array)

    # Aplica o counting sort para ordenar os elementos com base na posição
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

    return array


# Programa principal
if __name__ == "__main__":
    n = int(input("Insira o número de elementos do array: "))
    maximo = n * 10
    data = [random.randint(1, maximo) for _ in range(n)]

    print("Vetor original:", data)
    sorted_data = radixSort(data[:])
    print("Array ordenado:", sorted_data)
