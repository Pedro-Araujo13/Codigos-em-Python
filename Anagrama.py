palavra = []

pal = input("Insira uma palavra: ")

palavra = sorted(pal)

p = ""

for i in range(len(palavra)):
    l = palavra[i]
    p += l 
    
print(p)