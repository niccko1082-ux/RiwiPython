"""Tienda de camisetas
Una tienda vende camisetas a $20 cada una.

Si compras más de 10 camisetas → 12% de descuento.

Si compras más de 30 camisetas → 25% de descuento.

Si la cantidad ingresada es 0 o negativa → mostrar “Cantidad inválida”.
Calcular el total a pagar."""


camisa = 20000
cantidad = int(input("Ingresa la cantidad de camisas que deseas llevar: "))

if cantidad <= 0:
    print("Cantidad invalida")
elif cantidad < 10:
    descuento = camisa * cantidad

elif cantidad >= 10 and cantidad < 50:
    total = camisa * cantidad
    descuento = total - (total * 0.12)
else:
    total = camisa * cantidad
    descuento = total - (total * 0.25)

print(f"El valor total a pagar es de: ${descuento}")

