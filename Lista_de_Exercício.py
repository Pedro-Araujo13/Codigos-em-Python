import math
import random
import meu_modulo

def atividade01():
    soma_total = 0
    num_maior = 0
    num_menor = 0
    num = 0
    qtd_total = 0
    while True:
        
        num = int(input("Insira um número inteiro (ou digite 0 para sair): "))
        if num == 0:
            break
        soma_total += num
        if num > num_maior:
            num_maior = num
        if(num < num_menor or num_menor == 0):
            num_menor = num
        qtd_total += 1
    if qtd_total == 0:
        print("Fim do programa!")
    else:
        print(f"Maior valor: {num_maior} \nMenor Valor: {num_menor} \nNumeros totais digitados:{qtd_total} \nMédia dos valores: {soma_total/qtd_total}")

def atividade02():
    pessoas = {

    } 
    soma = 0
    contador = 0
    maior_idade = ("", 0)
    maior_18 = []
    menor_15 = []
    while True:
        nome = input("Insira o nome da pessoa(ou digite um valor negativo para sair): ")
        idade = int(input("Insira a idade da pessoa(ou digite valor negativo para sair): "))
        if idade < 0 or nome == "-":
            break
        pessoas[nome] = idade
    for chave, valor in pessoas.items():
        soma += valor
        contador += 1
        if valor > maior_idade[1]:
            maior_idade = (chave, valor)
        if valor >= 18:
            maior_18.append(chave)
        if valor <= 15:
            menor_15.append(chave)
    print(f"A média das idades é de {soma/contador:.2f}")
    print(f"A pessoa com a maior idade é: {maior_idade}")
    print(f"Pessoas com mais de 18 anos: {maior_18} \nPessoas com menos de 15 anos: {menor_15}")

def atividade03(raio):
    pi = 3.14
    return 2 * pi * raio*raio
def atividade03cont():
    for i in range(1,4):
        raio=float(input(f"Insira o {i}º raio em cm: "))
        print(f"A área do {i}º raio é: {atividade03(raio):.2f}cm")

def atividade04(num):
    if num == 0 or num == 1:
        return num
    else:
        return num * atividade04(num - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n - 1)
    
def atividade05():
    cont = "Sim"
    while cont.lower() in ("s", "sim"):
        n = int(input("Insira um número inteiro para sequência de Fibonacci: "))
        print(f"O {n}º termo da sequência de fibonacci é {fibonacci(n)}")
        cont = input("Deseja repetir com outro número? (Sim/Não): ")

def atividade06():

    print(math.sqrt(144))
    print(math.log(10))
    print(math.cos(math.radians(60)))

def atividade07():
    lista = []
    for i in range (1, 10):
        lancamento = random.randint(1,6)
        print(f"O {i}º lancamento é igual a: {lancamento}")
        lista.append(lancamento)
    lista.sort()
    print(lista)
    for i in range (1, 7):
        print(f"O número {i} se repetiu {lista.count(i)} veze(s)")

def atividade08():
    cont = "sim"
    while cont.lower() in ("sim", "s"):
        n1 = int(input("Insira um numero inteiro: "))
        n2 = int(input("Insira outro numero inteiro: "))
        if n2 == 0:
            print("Não é possível dividir por 0!")
        else:
            print(f"A divisão de {n1} por {n2} é igual a {(n1/n2):.2f}")
        cont = input("Digite 'Sim' para escolher outro par de numeros ou 'Não' para finalizar o prgrama: ")
    print("Fim do programa")

def atividade09():    
    for i in range (1, 6):
        n = int(input(f"Insira o {i}º número: "))
        if meu_modulo.checar_num(n):
            print(f"{n} é primo")
        else:
            print(f"{n} não é primo")

def atividade10():
    def cadastrar(dicionario, nome, matricula, curso): #recebe como parâmetros qual dicionário ele vai usar para cadastrar, e as outras informações necessárias
        dicionario[matricula] ={
            'nome': nome,
            'curso':curso
                }
        print("Cadastro Efetuado")

        ''' Vai receber um dicionário específico, e vai criar um dicionario aninhado (um dicionário dentro de outro dicionário)
        com a chave sendo a matrícula do estudante'''

    def atualizar(dicionario, matricula, dado, novo_dado): #recebe qual o dicionario, qual a matricula a ser procurada, qual a informação a ser alterada e qual vai ser a alteração
        ''' Função Atualizar:
        Vai pedir o dicionário, a matrícula (chave/dicionário) o dado a ser atualizado(chave do dicionário aninhado)
            e o novo dado.'''
        try:       
            for chave in dicionario[matricula]:
                if chave == dado:
                    dicionario[matricula][chave] = novo_dado
                    print("Atualização Realizada com sucesso!")
                    print(f"{dado}->{novo_dado}")
                else:
                    print(f"{dado} não encontrado!")
        except KeyError:
            print("Chave inválida")

            
    def excluir(dicionario, item_del): #recebe dicionário e o item a ser deletado
        try:
            del dicionario[item_del]
            print("Matrícula deletada com sucesso!")
        except KeyError:
            print("Chave Inválida")
        

    def listar(dicionario):
        for chave, itens in dicionario.items():
            print(chave, itens)

    estudantes = {
        '202503688291':{
            'nome': 'Pedro',
            'curso': 'Ciência da Computação'
        }
    } #inicializa o dicionário
    while True:
        print("--- Menu --- \n1.) Cadastrar Estudante \n2.) Atualizar Dados \n3.) Excluir \n4.) Listar \n0.) Sair ")
        opcao = int(input("Escolha uma opção: "))
        match opcao:

            case 1:
                matricula = input("Insira a matrícula do estudante: ")
                nome = input("Insira o nome: ")
                curso = input("Insira o curso: ")
                cadastrar(estudantes, nome, matricula, curso)
                for i, j in estudantes.items():
                    print(i, j)

            case 2:
                matricula = input("Insira a matrícula do aluno que você deseja atualizar informações: ")
                dado = input("Insira qual dado você deseja atualizar: ")
                novo_dado = input("Insira o novo dado: ")
                atualizar(estudantes, matricula, dado, novo_dado)
                for i, j in estudantes.items():
                    print(i, j)

            case 3: 
                item_del = input("Insira a matrícula que você quer deletar: ")
                excluir(estudantes, item_del)
                for i, j in estudantes.items():
                    print(i, j)
                    
            case 4:
                listar(estudantes)

            case 0:
                break

            case _:
                print("opcao inválida, tente novamente!")

    print(atualizar.__doc__)

atividade01()
atividade02()
atividade03cont()
print(atividade04(10))
atividade05()
atividade06()
atividade07()
atividade08()
atividade09()
atividade10()