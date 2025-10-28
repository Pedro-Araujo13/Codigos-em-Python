velocidade_vento = int(input("Insira a velocidade do vento da tempestade em km/h: "))

if velocidade_vento < 62: 
    print("Tempestade fraca")  
elif velocidade_vento >= 62 and velocidade_vento <= 118: 
    print("Tempestade Tropical") 
elif velocidade_vento >= 119 and velocidade_vento <=153:
    print("Furacão de categoria 1")
elif velocidade_vento >= 154 and velocidade_vento <= 177:
    print("Furacão de categoria 2")
elif velocidade_vento >= 178 and velocidade_vento <= 209:
    print("Furacão de categoria 3")
elif velocidade_vento >= 210 and velocidade_vento <= 249:
    print("Furacão de categoria 4")
elif velocidade_vento > 249:
    print("Furacão de categoria 5")
else:
    print("Valor inválido, tente novamente mais tarde!")