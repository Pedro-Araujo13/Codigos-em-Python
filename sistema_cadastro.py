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