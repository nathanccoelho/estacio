def smallNumber (lista):
    if not lista:
        return None  
    small = lista[0]  
    for i in lista:
        if i < small:
            small = i
    return small  
lista = [10, 3,5,4]

small = smallNumber(lista)
print(f"O menor número da lista é o {small}")