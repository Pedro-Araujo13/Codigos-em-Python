import os
os.system('clearsoc')
def palindromo():
    palavra = input("Insira uma palavra:  ")

    letras = []
    nova_palavra = ""
    for i in range (len(palavra)):
        letras.append(palavra[i])   

    letras.reverse()

    for i in letras:
        nova_palavra += i
    

    if nova_palavra == palavra:
        print(f"A {palavra} é um palindromo!")
    else:
        print(f"A {palavra} não é um palíndromo")


def maior_idade():
    idade = int(input("Insira sua idade: "))
    if idade < 18:
        adulto = input("Você está acompanhado por uma pessoa maior de 18 anos? (Sim ou Não): ")
        
        if adulto.lower() == "sim":
            print("Você pode entrar!")
        elif adulto.lower() == "não" or adulto.lower() == "nao":
            print("Você NÃO pode entrar!")
        else:
            print("Resposta Inválida")
    if idade >= 18:
        print("Você pode entrar!")

def lista_compras():
    lista_frutas = ["maca", "banana", "cereja"]
    print(lista_frutas[1])
    lista_frutas[0] = "kiwi"
    lista_frutas.append("laranja")
    lista_frutas.insert(1, "limão")
    lista_frutas.remove("banana")
    print(lista_frutas)

palindromo()
maior_idade()
lista_compras() 