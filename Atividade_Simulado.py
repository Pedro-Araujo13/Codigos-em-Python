def fatorial(n):
  if n in (0,1): 
    return n
  else:
    return n * fatorial(n-1)
  
print(fatorial(6))