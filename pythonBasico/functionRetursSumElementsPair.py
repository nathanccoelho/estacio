def totalInNumbersPair (lista):
    total = 0
    for elem in lista:
        if(elem%2==0):
            total+=elem
    return total

    
lista= [2,3,4,5,6,7,8]
totalPair = totalInNumbersPair(lista)

print(f"A soma dos números pares é: {totalPair}")