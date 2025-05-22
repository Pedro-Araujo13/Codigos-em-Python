proximoDigito = 0

num = int(input())

seqFibonacci = []

for n in range(num+1):
    if n != 0 and n != 1:
        n = seqFibonacci[n-2] + seqFibonacci[n - 1]  
    seqFibonacci.append(n)
seqFibonacci.remove(0
                    )
print(seqFibonacci)
