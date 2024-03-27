import random


class Binaria:
    def __init__(self):
        self.tamanho = 0
        self.vetor = []

    def cria_vetor(self, size):
        self.tamanho = size
        self.vetor = [random.randint(1, size * 9) for _ in range(self.tamanho)]
        self.vetor.sort()
        print("Vetor ordenado:", self.vetor)

    def pesquisa(self):
        print("Digite o número a pesquisar:")
        val = int(input())

        inicio, meio, fim = 0, 0, self.tamanho - 1
        iteracao = 1

        while inicio <= fim:
            print("\nIteração", iteracao)
            meio = (inicio + fim) // 2
            print("O nº do meio é:", self.vetor[meio])

            if val < self.vetor[inicio] or val > self.vetor[fim]:
                print("\nValor não encontrado!")
                print(f"Total de Iterações: {iteracao}\n")
                break
            elif val == self.vetor[meio]:
                print("\nEncontrou!")
                print(f"Total de Iterações: {iteracao}\n")
                break
            elif val > self.vetor[meio]:
                inicio = meio + 1
                print("{} é maior que {}, ele fica entre {} e {}\n".format(
                    val, self.vetor[meio], self.vetor[inicio], self.vetor[fim]))
            else:
                fim = meio - 1
                print("{} é menor que {}, ele fica entre {} e {}\n".format(
                    val, self.vetor[meio], self.vetor[inicio], self.vetor[fim]))
            iteracao += 1


# Exemplo de uso:
binaria = Binaria()
binaria.cria_vetor(60)
binaria.pesquisa()
