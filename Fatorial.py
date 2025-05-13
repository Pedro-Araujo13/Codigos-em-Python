fatorial = int(input(""))

resultado = 1

for i in range(1, fatorial + 1):
    resultado = (i * resultado)
print(resultado)