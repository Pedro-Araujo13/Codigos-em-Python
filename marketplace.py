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
    

'''sistema = Matricula()
sistema.matricularAluno()
for aluno in sistema.matriculas:
    print(aluno)'''
Curso.mostrarInfoCurso('CC')

curso01 = Curso("Natação", 890.99, 480, ["A - Manhã, B - Tarde, C - Noite"])
curso01.criarCurso()
Curso.mostrarCursos()
Curso.mostrarInfoCurso("Natação")