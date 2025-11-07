producto = 2000

cantidad = int(input("Ingresa la cantidad de de productos a comprar: "))

if cantidad > 30:
    valor = producto * cantidad
    descuento = valor - (valor * 0.15)
elif cantidad >= 10:
    valor = producto * cantidad
    descuento = valor - (valor * 0.05)
else:
    valor = producto * cantidad
    print(f"El valor total bruto: {valor}")
    print(f"El valor total con envio es de: {valor + 5000}")
    exit()

if descuento < 50000:
    print(f"Valor total bruto: {valor}")
    print(f"valor total con descuento: {descuento}")
    envio = descuento + 5000
    print(f"valor total con envio: {envio}")
else:
    print(f"Valor total bruto: {valor}")
    print(f"valor total con descuento: {descuento}")
    print("el envio es gratis")
