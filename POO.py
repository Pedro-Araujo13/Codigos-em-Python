class Conta():
    def __init__(self,num_conta, saldo):
        self.num_conta = num_conta
        self.saldo = saldo
    
    def debitar(self, valor):
        self.saldo = self.saldo - valor
    
    def creditar(self, valor):
        self.saldo = self.saldo + valor

conta1 = Conta("123456", 5000)
print(conta1.saldo)
conta1.debitar(750)
print(conta1.saldo)
conta1.creditar(1000)
print(conta1.saldo)

class Calculadora():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self):
        return self.num1 + self.num2
    
    def subtracao(self):
        return self.num1 - self.num2

    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return print("Impossível dividir por 0")


operacao = Calculadora(1, 0)
print(operacao.somar())
print(operacao.subtracao())
print(operacao.multiplicacao())
print(operacao.divisao())

class Funcionario():
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.salario = 2000

class Gerente(Funcionario):
    def __init__(self, nome, cpf, idade, equipe):
        super().__init__(nome, cpf, idade)
        self.equipe = equipe
        self.salario = self.salario * 1.15

class Diretor(Funcionario):
    def __init__(self, nome, cpf, idade, setor):
        super().__init__(nome, cpf, idade)
        self.setor = setor
        self.salario = self.salario * 1.15

class Secretario(Funcionario):
    def __init__(self, nome, cpf, idade, sala):
        super().__init__(nome, cpf, idade)
        self.sala = sala
        self.salario = self.salario * 1.1

class Presidente(Funcionario):
    def __init__(self, nome, cpf, idade, empresa):
        super().__init__(nome, cpf, idade)
        self.empresa = empresa 
        self.salario = self.salario * 1.1


pessoa1 = Gerente("Carlos", "123", 22, "Red")
pessoa2 = Diretor("José", "321", 27, "A")
pessoa3 = Secretario("Amanda", "456", 32, "Food LTDA")
pessoa4 = Presidente("Raquel", "987", 47, "Company")

print(pessoa2.salario)
print(pessoa1.salario)
print(pessoa3.salario)
print(pessoa4.salario)