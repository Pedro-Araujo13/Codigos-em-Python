import os
os.system('cls')

#par ou impar

'''
num = int(input())

if num % 2 == 0:
    print("Número Par!")
else:
    print("Número Impar!")
'''

#contador de vogais
'''
text = input()
contador = 0
vogais = "aeiouAEIOU"
for letra in text:
    if letra in vogais:
        contador += 1
print(f"A quantidade de vogais é de: {contador}")'''

#contador de vogais avançado
palavra = input()
vogais = "aeiouAEIOU"
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for letra in palavra:
    if letra in vogais:
        if letra == 'a':
            contador_a += 1
        elif letra == 'e':
            contador_e += 1
        elif letra == 'i':
            contador_i += 1
        elif letra == 'o':
            contador_o += 1
        elif letra == 'u':
            contador_u += 1



print(f"A: {contador_a} \nE: {contador_e}\nI: {contador_i}\nO: {contador_o}\nU: {contador_u}")
print(contador_u + contador_a + contador_e + contador_i + contador_o)