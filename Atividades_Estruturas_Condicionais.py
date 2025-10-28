def NotaAuluno ():
    n1 = float(input("Insira a primeira nota: "))
    n2 = float(input("Insira a segunda nota: "))
    media = (n1 + n2) / 2
    print(f"Sua média foi {media}! ")
    if  media >= 7:
        print("Aluno Aprovado!")
    elif media >= 3 and media < 7:
        nota_final = float(input("Aluno em recuperação, será necessário informar a nota da prova final!: "))
        if nota_final + media >= 5:
            print(f"Sua média final foi: {nota_final + media}")
            print("Aluno Aprovado!")
        else: 
            print("Aluno Reprovado!")
    elif media < 3:
        print("Aluno reprovado!")
    
def AlturaAluno():
    i = 10
    altura_max = 0
    altura_min = 0
    media = 0
    for j in range(i):
        altura = float(input(f"Insira a aultura do {j + 1}º estudante: "))
        media += altura
        if altura > altura_max:
            altura_max = altura
        if altura < altura_min or altura_min == 0:
            altura_min = altura

    media_final = (media / i)
    print(f"A Média final é: {media_final:.2f}")
    print(f"A Altura máxima é: {altura_max}")
    print(f"A Altura mínima é: {altura_min}")

#NotaAuluno()
#AlturaAluno()
