def checar_num(numero):
    if numero % 2 == 0:
        print(f"{numero} é par")
    elif numero == 0:
        print(f"{numero} é neutro")
    else:
        print(f"{numero} é impar")

    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
    