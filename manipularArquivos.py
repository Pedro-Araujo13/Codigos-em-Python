import os
os.system('cls')

with open("lista_de_compras.txt", "r") as archive:
    compras = archive.readlines()
    for i in compras:
        print(f"Item: {i.strip()}") 
continuar = input("deseja registrar um novo item? (s/n)?")

while continuar.lower() == 's':

    with open("lista_de_compras.txt", "a") as archive:
        item = input("insira o novo item que deseja registrar: ")
        archive.write(f"\n{item}")

    with open("lista_de_compras.txt", "r") as archive:
        compras = archive.readlines()
        for i in compras:
            print(f"Item: {i.strip()}")
        continuar = input("deseja registrar um novo item? (s/n)?")
