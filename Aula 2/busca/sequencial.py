#algoritmo de busca sequencial
import random

tamanho = 300
procurado = 789

#criar um array
numeros_unicos = set()
while len(numeros_unicos) < tamanho:
    numeros_unicos.add(random.randint(1, 900))
array = list(numeros_unicos)

#ordenando o array
array.sort()

#exibir o array na tela
print("Exibindo o array na tela:")
print(" - ".join(map(str, array)))

#implementar a busca sequencial
iteracoes = 0

encontrado = False
for i in range(len(array)):
    iteracoes += 1
    if array[i] == procurado:
        encontrado = True
        break

#exibindo na tela
if encontrado:
    print(f"Número {procurado} encontrado na posição {i} do Array.")
else:
    print(f"Numero {procurado} não foi encontrado.")

print(f"Tentativas: {iteracoes}")        