import random

class Binaria:
    def __init__(self):
        self.tamanho = 0
        self.vetor = []

    #algoritmo de criação do vetor ordenado
    def cria_vetor(self, size):
        self.tamanho = size
        self.vetor = [random.randint(1, size * 10) 
    for _ in range(self.tamanho)]
        self.vetor.sort() #preguiça
        print("Vetor ordenado:", self.vetor)

    #algoritmo da pesquisa binária
    def pesquisa(self):
        print("Digite o número a ser encontrado:")
        val = int(input())   

        inicio, meio, fim = 0, 0, self.tamanho - 1
        iteracao = 1

        while inicio <= fim:
            print("\nIteração", iteracao)
            meio = (inicio + fim) // 2
            print("O nº do meio é", self.vetor[meio])

            #não encontrado
            if val < self.vetor[inicio] or val > self.vetor[fim]:
                print("\nValor não encontrado!")
                print(f"Total de iterações: {iteracao} \n")
                break

            #encontrou
            elif val == self.vetor[meio]:
                print("\nValor Encontrado!")
                print(f"Total de iterações: {iteracao} \n")
                break

            elif val > self.vetor[meio]: #maior que a raiz
                inicio = meio + 1
                print("{} é maior que {}, fica entre {} e {}.\n"
                      .format(
                            val, self.vetor[meio], 
                            self.vetor[inicio], 
                            self.vetor[fim]
                            ))  
                            
            else:  #menor que o meio
                inicio = meio - 1
                print("{} é menor que {}, fica entre {} e {}.\n"
                      .format(
                            val, self.vetor[meio], 
                            self.vetor[inicio], 
                            self.vetor[fim]
                            ))  
            iteracao += 1

#execução
binaria = Binaria()
binaria.cria_vetor(50)        
binaria.pesquisa()


