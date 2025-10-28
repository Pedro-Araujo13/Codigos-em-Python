import os
import random
import math
os.system('clear')

def atividade01():
    def tabuada(n):
        print(f"A tabuada do número {n} é: \n")
        for i in range(1,11):
            print(f"{n} x {i} = {n*i}")
        return 0

    while True:
        continuar = input("Pressione Enter para continuar (ou 'sair' para encerrar): ") 
        if continuar.lower() == 'sair':
            break
        n = int(input("Insira um número inteiro para tabuada: "))       
        print(tabuada(n))
    return 0



def atividade02():
    numero = random.randrange(1,50)
    print("NUMERO SORTEADO!")
    num = int(input("Digite um número inteiro entre 1 e 50 para tentar sua sorte: "))
    if num == numero:
        print("Parabéns, Você acertou de primeira! Campeão!")
    else:
        while num != numero:
            if num > numero:
                num = int(input(f"o número sorteado é menor que {num}: "))
            elif num < numero:
                num = int(input(f"o número sorteado é maior que {num}: "))
            else:
                break
        print("Parabéns! Você acertou!!")
    return 0


def calculadora(op,x,y):

    operators = {
        "multiplicação": print(x * y),
        "soma": print(x + y),
        "subtração": print(x - y),
        "potência": print(pow(x, y))
    }

    for x, y in operators.items():
        if op == x:
            return y


calculadora("potência", 3, 2)

