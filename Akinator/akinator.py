class Akinator:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.vetor = [i + 1 for 
        i in range(tamanho)]
        self.inicio = 0
        self.fim = tamanho - 1
        self.meio = 0

    #criação do vetor
    def preencherVetor(self):
        self.vetor = [i + 1 for 
        i in range(self.tamanho)]

    #mostrar o vetor
    def mostraVetor(self):
        print(" - ".join(map(str,self.vetor))) 


    #funcao akinator
    def Akinator(self):
        self.inicio = 0;
        self.fim = len(self.vetor) - 1

        print("\nDIGITE 9 SE EU ACERTEI, 0 SE FOR MENOR E 1 SE FOR MAIOR: \n")
        iter = 1

        while self.inicio <= self.fim:
            self.meio = (self.inicio + self.fim) // 2
            val = int(input(f"Tentativa {iter} - O número é {self.vetor[self.meio]}? "))  
            
            #decisao da árvore binária
            if val == 9:
                print(f"Valor encontrado! \n Total de tentativas: {iter} \n FIM DE JOGO!")
                break
            elif val == 1:
                self.inicio = self.meio + 1
            elif val == 0:
                self.fim = self.meio - 1    
            else:
                print("Não entendi!")
            iter += 1    


 #iniciar
tamanho_vetor = int(input("Digite o tamanho do vetor: "))
jogo = Akinator(tamanho_vetor)
jogo.preencherVetor()
#print("Vetor inicial:")
#jogo.mostraVetor()   
jogo.Akinator()        