from abc import ABC, abstractmethod
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
    listaCursos = ["CC", "ADS", "ENFERMAGEM"] #a lsita precisa ser declarada aqui pois do contrário, seria considerada uma instância da Classe, coisa q não é
    
    informacoesCursos = {
        'CC': { 
            'Preco' : 1800,
            'Carga Horaria': 360,
            'Turmas' : ["A", "C"]
        },
        'ADS': {
            'Preco' : 800,
            'Carga Horaria': 180,
            'Turmas' : ["A", "B", "C"]
        },
        'ENFERMAGEM': {
            'Preco' : 2100,
            'Carga Horaria': 580,
            'Turmas' : ["A", "B"]
        }
    }

    def __init__(self,nome, preco, cargaHoraria,turmas):
        self.nome = nome
        self.preco = preco
        self.cargaHoraria = cargaHoraria
        self.turmas = turmas

    def criarCurso(self):
        Curso.listaCursos.append(self.nome)
        Curso.informacoesCursos[self.nome] = {
            'Preco': self.preco,
            'Carga Horaria': self.cargaHoraria,
            'Turmas': self.turmas
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
        
    def mostrarTurmas(cursoDesejado):
        return Curso.informacoesCursos[cursoDesejado]['Turmas']
    
    def cadastrarTurmas(curso, turmas):
       turmasList = Curso.informacoesCursos[curso]['Turmas']
       turmasList.extend(turmas)


class Pagamento():
    def __init__(self):
        self.faturamento = []
        
        def processarPagamento(self):
            print("Processando pagamento!")
            print("Pagamento Efetuado")

class Pix(Pagamento):
    def __init__(self, aluno, chavePix):
        super().__init__(aluno)
        self.chavePix = chavePix

class CartaoCredito(Pagamento):
    def __init__(self, aluno, numeroCartao):
        super().__init__(aluno)
        self.numeroCartao = numeroCartao
        
class Boleto(Pagamento):
    def  __init__(self, aluno, cpf):
        super().__init(aluno)
        self.cpf = cpf 

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
        pagamento = input("Forma Pagamento: Pix, Cartão de Crédito, Boleto: ")
        novoAluno = Aluno(alunoNome,cpf, telefone, curso, turma, matricula, pagamento)
        self.matriculas.append(novoAluno)
        print("Aluno Matriculado com sucesso!")

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
        self.cadastrarOrganizador.append(novoOrganizador)

sistema = Matricula()
sebastiao = Organizador("Sebastião", "71065600496", 81989489744)
