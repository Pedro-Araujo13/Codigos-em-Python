def longestCommonPrefix(strs:list):
    if not strs: #Se nada for inserido no input
        return "" #return ""
    
    prefixo = strs[0] #declara o prefixo como a primeira palavra da lista

    for i in range(1, len(strs)): #vai começar a iterar a partir do segundo item da lsita até o final
        palavra = strs[i] # A palavra a ser analisada

        while not palavra.startswith(prefixo): #Enquanto a palavra da vez não começar com o prefixo preestabelecido
           
           prefixo = prefixo[:-1] # o prefixo vai diminuir uma letra a cada iteração

           if not prefixo: # e caso não reste nada em prefixo
               return "" #vai "matar a função, pois se uma não tem o prefixo igual, então nem adianta conferir o restante. 
           #TODOS OS ELEMENTOS DA LISTA PRECISAM TER O MESMO PREFIXO COMUM!
           
    return(prefixo) # e caso chegue aqui, significa que restou um prefixo comum em todas as palavras

print(longestCommonPrefix(["red", "redencao", "read"]))
