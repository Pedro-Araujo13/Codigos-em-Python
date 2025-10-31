from abc import ABC, abstractmethod
import time
import os
class Usuario(ABC): #Classe Abstrata de Usuário
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
     
class Aluno(Usuario):
    def __init__(self, nome, cpf, telefone, curso, turma, matricula, pagamento):
        super().__init__(nome, cpf, telefone)
        self.curso = curso
        self.turma = turma
        self.pagamento = pagamento
        self.matricula = matricula

    def __str__(self): #Função reservada para converter o objeto em str e poder ser armazenado de forma legível na lista de matrículas
        return f"Nome: {self.nome} - CPF: {self.cpf} - Tel: {self.telefone} - Curso: {self.curso} - Turma: {self.turma} - Matrícula: {self.matricula} - Pagamento: {self.pagamento}"

class Organizador(Usuario):
    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)

    def criarCurso(self):
        curso = input("Nome do Curso: ").upper()
        preco = float(input("Preço do curso: "))
        cargaHoraria = int(input("Carga Horaria: "))
        turma = []
        qtdTurma = int(input("Insira quantas turmas serão adicionadas inicialmente: "))
        for i in range(qtdTurma):
            turmaNome = input(f"Insira a {i+1}º turma: ")
            turma.append(turmaNome)
        cursoClass = Curso(curso, preco, cargaHoraria, turma)
        cursoClass.criarCurso()

    def cadastrarTurma(self):
        turmasList = []
        Curso.mostrarCursos()
        curso = input("Deseja cadastrar turmas em qual curso?: ").upper()
        while Curso.percorrerCursos(curso) != True:
            curso = input("Curso Inexistente. Insira um curso válido: ").upper()
        qtdTurma = int(input("Insira quantas turmas você deseja cadastrar: "))
        for i in range(qtdTurma):
            turma = input(f"Insira a {i+1}ª turma: ")
            turmasList.append(turma)
        Curso.cadastrarTurmas(curso, turmasList)

    def __str__(self):
        return f"Nome: {self.nome} - CPF: {self.cpf} - Tel: {self.telefone}"

class Instrutor(Usuario):
    def __init__(self, nome, cpf, telefone, curso, turma):
        super().__init__(nome, cpf, telefone)
        self.curso = curso
        self.turma = turma

    def __str__(self):
        return f"Nome: {self.nome} - CPF: {self.cpf} - Tel: {self.telefone} - Curso de Atuação: {self.curso} - Turma Vinculada: {self.turma}"
  

class Curso():
    listaCursos = ["CC"] #a lsita precisa ser declarada aqui pois do contrário, seria considerada uma instância da Classe, coisa q não é
    
    informacoesCursos = {
        'CC': { 
            'Preco' : 1800,
            'Carga Horaria': 360,
            'Turmas' : {
                'A' : [],
                'B' : []
            }
        }
        }

    def __init__(self,nome, preco, cargaHoraria,turmas):
        self.nome = nome
        self.preco = preco
        self.cargaHoraria = cargaHoraria
        self.turmas = {turma: [] for turma in turmas}
    def criarCurso(self):
        Curso.listaCursos.append(self.nome)
        Curso.informacoesCursos[self.nome] = {
            'Preco': self.preco,
            'Carga Horaria': self.cargaHoraria,
            'Turmas': 
                self.turmas2
        
            }
        
        
    @staticmethod #serve para mostrar que o método faz parte da classe, mas não precisa de nenhuma instância
    def mostrarCursos():
        print(Curso.listaCursos) #funcao para mostrar os cursos disponíveis

    def percorrerCursos(cursoDesejado):
        for curso in Curso.listaCursos:
            if cursoDesejado == curso:
                return True
            
    def mostrarInfoCurso(cursoDesejado):
        if cursoDesejado in Curso.informacoesCursos:
            for chave, valor in Curso.informacoesCursos[cursoDesejado].items():
                print(f"{chave} - {valor}")
        else:
            print("Curso não encontrado!")
    def mostrarInfoGeral():
        for chave, valor in Curso.informacoesCursos.items():
            print(f"{chave} - {valor}")

    def mostrarTurmas(cursoDesejado):
        return Curso.informacoesCursos[cursoDesejado]['Turmas']
    
    def cadastrarTurmas(curso, turmas):
       for c in turmas:
           Curso.informacoesCursos[curso]['Turmas'][c] = []



class Pagamento():
    faturamentoTotal = 0
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.faturamento = []
    def processarPagamento(self):
        print("Processando pagamento!")
        print("Pagamento Efetuado")
    @staticmethod
    def relatorioFaturamento():
        print(f"O faturamento atual do MarketPlace Wyden é de R${Pagamento.faturamentoTotal}")

class Pix(Pagamento):
    
    def __init__(self, aluno, cpf):
        super().__init__(aluno, cpf)
       

    def processarPagamento(self, sistema):
        curso = sistema.buscarCPF(self.cpf)  #Se a funçao retorna o curso, eu posso pesquisar o valor do curso pela função e somar na lista self.faturamento lá na função de pagamento
        print(f"Gerando chave pix...")
        time.sleep(1)
        valor = Curso.informacoesCursos[curso]['Preco']
        print(f"Chave pix: 12345678910 \nValor: {valor}")
        pagamento = input("Pressione 's' para continuar com pagamento ou 'n' para cancelar: ").lower()
        if pagamento == 's':
            Pagamento.faturamentoTotal += valor
            print(f"Pagamento Efetuado com sucesso!")
            sistema.cadastrarAlunoTurma(self.cpf)
            

class CartaoCredito(Pagamento):
    def __init__(self, aluno, cpf, numeroCartao):
        super().__init__(aluno, cpf)
        self.numeroCartao = numeroCartao

    def processarPagamento(self, sistema):
        curso = sistema.buscarCPF(self.cpf) 
        time.sleep(1)
        valor = Curso.informacoesCursos[curso]['Preco']
        input("Insira o número do cartão: ")
        print(f"Cobrança chegará em conta em até 24H, Valor: R${valor}")
        pagamento = input("Pressione 's' para continuar com pagamento ou 'n' para cancelar: ").lower()
        if pagamento == 's':
            Pagamento.faturamentoTotal += valor
            print(f"Pagamento Efetuado com sucesso!")
            sistema.cadastrarAlunoTurma(self.cpf)
        
class Boleto(Pagamento):
    def  __init__(self, aluno, cpf):
        super().__init(aluno, cpf)


    def processarPagamento(self, sistema):
        curso = sistema.buscarCPF(self.cpf) 
        time.sleep(1)
        valor = Curso.informacoesCursos[curso]['Preco']
        print(f"<link do Boleto> R${valor}")
        print(f"Você tem até 3 dias úteis para realizar o pagamento do Boleto!")
        pagamento = input("Pressione 's' para continuar com pagamento ou 'n' para cancelar: ").lower()
        if pagamento == 's':
            Pagamento.faturamentoTotal += valor
            print(f"Pagamento Efetuado com sucesso!")
            sistema.cadastrarAlunoTurma(self.cpf)

class Matricula():
    def __init__(self):
        self.matriculas = []
        self.matriculasInstrutor = []
        self.matriculasOrganizador = []

    def matricularAluno(self):
        matricula = ""
        ano = "2025"
        alunoNome = input("Nome: ")
        telefone = input("Número Telefone: ")

        while True: #Laço para capturar erros do cpf
            cpf = input("CPF (Somente Números): ")

            if not cpf.isdigit():
                print("O cpf deve conter apenas números!")
                continue
            
            if len(cpf) != 11:
                print("O CPF deve conter 11 números!")
                continue

            break

        Curso.mostrarCursos()
        curso =  input("Curso: ").upper()

        while Curso.percorrerCursos(curso) != True: #Laço para capturar erros do campo 'curso'
            Curso.mostrarCursos()
            curso = input("Curso Inexistente ou Inválido, Escolha um da presente lista: ").upper()
        
        print(Curso.mostrarTurmas(curso)) 

        while True:
            turma = input("Turma: ").upper()
            if turma not in Curso.mostrarTurmas(curso):
                print("Turma não encontrada! Selecione uma existente")
                continue
            break
            
        i = 0
        while i < 6:
            matricula += cpf[i]
            i+=1
        matricula += ano
        novoAluno = Aluno(alunoNome,cpf, telefone, curso, turma, matricula, None)
        self.matriculas.append(novoAluno)
        pagamentoOption = int(input("Forma Pagamento: \n1-Pix \n2-Cartão de Crédito \n3-Boleto: "))
        match (pagamentoOption):
            case 1:
                pagamento = Pix(alunoNome, cpf)
                realizarPagamento = input("Deseja realizar pagamento agora? (s/n): ").lower()
                if realizarPagamento == 's':
                    pagamento.processarPagamento(self)
                    print("Aluno matriculado com sucesso!")
                    time.sleep(2)
                elif realizarPagamento == 'n':
                    pagamento = False
                    print("Aluno Cadastrado com sucesso, pagamento pendente")
                    time.sleep(2)
            case 2:
                numCartao = input("Insira o número do cartão: ")
                pagamento = CartaoCredito(alunoNome, cpf, numCartao)
                print(pagamento.cpf)
                realizarPagamento = input("Deseja realizar pagamento agora? (s/n)").lower()
                if realizarPagamento == 's':
                    pagamento.processarPagamento(self)
                    print("Aluno matriculado com sucesso!")
                    time.sleep(2)
                elif realizarPagamento == 'n':
                    pagamento = False
                    print("Aluno Cadastrado com sucesso, pagamento pendente")
                    time.sleep(2)
            case 3:
                pagamento = Boleto(alunoNome, cpf)
                print(pagamento.cpf)
                realizarPagamento = input("Deseja realizar pagamento agora? (s/n)").lower()
                if realizarPagamento == 's':
                    pagamento.processarPagamento(self)
                    print("Aluno matriculado com sucesso!")
                    time.sleep(2)
                    
                elif realizarPagamento == 'n':
                    pagamento = False
                    print("Aluno Cadastrado com sucesso, pagamento pendente")
                    time.sleep(2)
                    
            case _:
                print("Opção Invália!")
        
        novoAluno.pagamento = pagamento
        
    def cadastrarInstrutor(self):
        instrutorNome = input("Nome do Instrutor: ")

        while True: #Laço para capturar erros do cpf
            cpfInstrutor = input("CPF do Instrutor(Somente Números): ")
            if not cpfInstrutor.isdigit():
                print("O cpf deve conter apenas números!")
                continue
            if len(cpfInstrutor) != 11:
                print("O CPF deve conter 11 números!")
                continue
            break
        telInstrutor = input("Número de Telefone do Instrutor: ")
        Curso.mostrarCursos()
        cursoInstrutor = input("Insira o curso que o Instrutor leciona: ").upper()

        while Curso.percorrerCursos(cursoInstrutor) != True: #Laço para capturar erros do campo 'curso'
            Curso.mostrarCursos()
            cursoInstrutor = input("Curso Inexistente ou Inválido, Escolha um da presente lista: ").upper()

        coursesClasses = Curso.mostrarTurmas(cursoInstrutor)
        print(coursesClasses)
        while True:
            turmaInstrutor = input("Insira qual turma o instrutor vai se vincular: ").upper()
            if turmaInstrutor not in Curso.mostrarTurmas(cursoInstrutor):
                print("Turma não encontrada! Selecione uma existente")
                continue
            break
        novoInstrutor = Instrutor(instrutorNome, cpfInstrutor, telInstrutor, cursoInstrutor, turmaInstrutor)
        self.matriculasInstrutor.append(novoInstrutor)
        print("Instrutor cadastrado com sucesso!")

    def cadastrarOrganizador(self):
        nomeOrganizador = input("Insira o nome do Organizador: ")

        while True: #Laço para capturar erros do cpf
            cpfOrganizador = input("CPF do Instrutor(Somente Números): ")
            if not cpfOrganizador.isdigit():
                print("O cpf deve conter apenas números!")
                continue
            if len(cpfOrganizador) != 11:
                print("O CPF deve conter 11 números!")
                continue
            break
        telOrganizador = input("Insira o número celular do organizador: ")

        novoOrganizador = Organizador(nomeOrganizador, cpfOrganizador, telOrganizador)
        self.matriculasOrganizador.append(novoOrganizador)
        print("Organizador Cadastrado com sucesso!")
        time.sleep(2)

    def buscarCPF(self, cpfBuscado): #Buscar o curso de um aluno específico pelo CPF
        for aluno in self.matriculas:
            if aluno.cpf == cpfBuscado:
                
                return aluno.curso #retorna o curso do determinado aluno
    def cadastrarAlunoTurma(self, cpfBuscado):
        for aluno in self.matriculas:
            if aluno.cpf == cpfBuscado:
                Curso.informacoesCursos[aluno.curso]['Turmas'][aluno.turma].append(aluno.nome)



class MenuPrincipal():
    pass
   
    def menuPrincipal():
        sistema = Matricula()
        while True:
            print("### BEM-VINDO AO MARKETPLACE WYDEN ####\n")
            print("1 - Painel do Aluno. ")
            print("2 - Painel do Organizador.")
            print("3 - Listar Cursos e Turmas.")
            print("4 - Faturamento total. ")
            print("5 - Cadastrar Instrutor")
            print("6 - Cadastrar Organizador")
            print("7 - Encerrar Sistema. ")
            opcao = int(input("Opcao: "))
            match (opcao):
                case 1:
                    os.system('clear')
                    sistema.matricularAluno()
                case 2:
                    os.system('clear')
                    if sistema.matriculasOrganizador:
                        print("### MARKETPLACE WYDEN ###")
                        print("--- Área do Organizador ---\n")
                        print("1 - Cadastrar curso ")
                        print("2 - Cadastrar turma")
                        print("3 - Sair")
                        opcao =  int(input("Opcao: "))
                        match (opcao):
                            case 1:
                                os.system('clear')
                                organizador = sistema.matriculasOrganizador[0]
                                organizador.criarCurso()
                            case 2:
                                os.system('clear')
                                organizador = sistema.matriculasOrganizador[0]
                                organizador.cadastrarTurma()
                            case 3:
                                os.system('clear')
                                print("Saindo...")
                                time.sleep(1)
                    else:
                        print("É preciso cadastrar um Organizador primeiro!")
                case 3:
                    os.system('clear')
                    Curso.mostrarInfoGeral()
                case 4:
                    os.system('clear')
                    Pagamento.relatorioFaturamento()
                case 5:
                    os.system('clear')
                    sistema.cadastrarInstrutor()
                case 6:
                    os.system('clear')
                    sistema.cadastrarOrganizador()
                case 7:
                    os.system('clear')
                    print("Saindo do sistema...")
                    time.sleep(2)
                    break
MenuPrincipal.menuPrincipal()      
            
                    
            


