class Usuario(): #Classe Abstrata de Usuário
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        #Listas para serem adionados os instrutores e organizadores
        self.instrutores = []
        self.organizadores =[]

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
    def __init__(self, nome, cpf, telefone, area):
        super().__init__(nome, cpf, telefone)
        self.area = area #area de atuacao

class Instrutor(Usuario):
    def __init__(self, nome, cpf, telefone, curso, turma):
        super().__init__(nome, cpf, telefone)
        self.curso = curso
        self.turma = turma

class Curso():
    listaCursos = ["CC", "ADS", "ENFERMAGEM"] #a lsita precisa ser declarada aqui pois do contrário, seria considerada uma instância da Classe, coisa q não é

    def __init__(self, preco, cargaHoraria):
        self.preco = preco
        self.cargaHoraria = cargaHoraria
        #listas para receber turmas associadas e cursos da instituição
        self.turmaAssociada = []
        
    @staticmethod #serve para mostrar que o método faz parte da classe, mas não precisa de nenhuma instância
    def mostrarCursos():
        print(Curso.listaCursos) #funcao para mostrar os cursos disponíveis

    def percorrerCursos(cursoDesejado):
        for curso in Curso.listaCursos:
            if cursoDesejado == curso:
                return True


class Turma():
    def __init__(self, dataInicio, instrutor, vagasQuantidade):
        self.dataInicio = dataInicio
        self.instrutor = instrutor
        self.vagasQuantidade = vagasQuantidade
    
class Pagamento():
    def __init__(self, aluno):
        self.aluno = aluno

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

    def matricularAluno(self):
        matricula = ""
        ano = "2025"
        alunoNome = input("Nome: ")
        telefone = input("Número Telefone: ")
        cpf = input("CPF: ")
        Curso.mostrarCursos()
        curso =  input("Curso: ").upper()
        while Curso.percorrerCursos(curso) != True:
            Curso.mostrarCursos()
            curso = input("Curso Inexistente ou Inválido, Escolha um da presente lista: ").upper()

        turma = input("Turma: ")
        i = 0
        while i < 6:
            matricula += cpf[i]
            i+=1
        matricula += ano
        pagamento = input("Forma Pagamento: Pix, Cartão de Crédito, Boleto: ")
        novoAluno = Aluno(alunoNome,cpf, telefone, curso, turma, matricula, pagamento)
        self.matriculas.append(novoAluno)
        print("Aluno Matriculado com sucesso!")
    

sistema = Matricula()
sistema.matricularAluno()
for aluno in sistema.matriculas:
    print(aluno)