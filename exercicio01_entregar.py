#Exercícios
#1) Gerar um número de 1 a 100, e solicitar para que o usuário tente adivinhar o número.



#Exercício 1



import random


def gera():
    return random.randint(1, 100)


def game():
    resposta = gera()
    tentativa = 0
    print("\nPalpite gerado!")

    chute = 0
    while chute is not resposta:
        tentativa += 1
        chute = int(input("Qual seu chute: "))
        if chute > resposta:
            print("Errou! É um valor menor que ", chute)
        elif chute < resposta:
            print("Errou! É um valor maior que ", chute)
        else:
            print("Parabéns! O número gerado foi ", resposta, \
                  "Acertou em ", tentativa, " tentativas!")
            break

while True:
    game()
    print()



