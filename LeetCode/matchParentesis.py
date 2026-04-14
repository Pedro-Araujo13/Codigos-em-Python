def isValid(s:str):

    topStack = ["(", "[", "{" ]
    auxiliarList = ["()", "[]", "{}"]
    stackString = []

    for i in s[::1]:
        if i in topStack:
            stackString.append(i)
        elif stackString and (stackString[-1] + i in auxiliarList) :
            stackString.pop()
        else:
            return False
    
    if not stackString: 
        return True
    return False
        
