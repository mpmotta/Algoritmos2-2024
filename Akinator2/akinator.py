import sys

from personagens import get_personagens


class Akinator:
    def __init__(self):
        self.database = get_personagens()

    def perguntas(self):
        Perguntas = [
            ["humano", "É um ser humano? "],
            ["ruivo", "É ruivo? "],
            ["princesa", "É príncipe/princesa? "],
            ["vampiro", "É vampiro(a)? "],
            ["oculos", "Usa óculos? "],
            ["loiro", "É loiro(a)? "],
            ["rabo", "Possui rabo? "],
            ["fome", "Vive com fome? "],
            ["aventura", "É do desenho Hora de Aventura? "],
            ["magico", "É mágico? "],
            ["coragem", "É corajoso(a)? "],
            ["homem", "É homem? "],
            ["hogwarts", "É de Hogwarts? "],
            ["velho", "É velho? "],
            ["scooby", "É da turma do Scooby-Doo? "],
            ["twilight", "É da saga Crepúsculo? "],
            ["heroi", "É um Super Herói? "],
            ["verde", "É verde? "],
            ["armadura", "Usa Armadura? "],
            ["superpoder", "Tem algum Superpoder? "]
        ]

        print("1 PARA SIM E 0 PARA NÃO!")
        for pergunta in Perguntas:
            resposta = input(pergunta[1])
            self.verifica(int(resposta), pergunta[0], self.database)

    def verifica(self, resposta, propriedade, database):
        ans = bool(resposta)

        remover = []
        for d in database:
            prop = d[propriedade]
            if prop != ans:
                remover.append(d)

        for ch in remover:
            database.remove(ch)

        if not database:
            print("Não consegui descobrir!")
            return
        elif len(database) == 1:
            personagem = database[0]
            nome = personagem["nome"]
            print(f"O Personagem é {nome}")
            print("\nFIM DE JOGO")
            sys.exit()


# Inicialização e execução do jogo
jogo = Akinator()
jogo.perguntas()
