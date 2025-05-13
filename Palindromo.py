texto = input()
lista = []
new_word = ""

for indice in range(len(texto)):
	lista.append(texto[indice])
	

lista.reverse()

for i in range(len(lista)):
	new_word += lista[i]


if (new_word == texto):
	print("True")
else:
	print("False")