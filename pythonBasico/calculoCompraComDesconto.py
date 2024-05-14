price = 10.0

compra = int(input("Quantidade desejada: "))

def calcular(quantity, price):
    return quantity*price

def desconto(valor, porcentagem):
     valor_subtraido = valor * (porcentagem / 100)
     return valor - valor_subtraido

if compra > 10 and compra <=20:
    newPrice = calcular(compra, price)
    priceComDesconto = desconto(newPrice,10)
    print(f"Valor total: {priceComDesconto} ")
elif(compra > 20):
    newPrice = calcular(compra, price)
    priceComDesconto = desconto(newPrice,20)
    print(f"Valor total: {priceComDesconto} ")
else:
    newPrice = calcular(compra, price)
    print(f"Valor total: {newPrice} ")