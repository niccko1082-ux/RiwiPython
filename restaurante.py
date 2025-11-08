"""7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA
Menú: $12.000

Opciones bebida:

sí → $3.000
no → $0
Luego aplicar IVA del 8% al total final.
Mostrar valor con IVA incluido.
"""

menu = 12000
bebida = 3000

opcional = input("deseas incluir bebida en el menu (si/no)").lower()

if opcional == "si":
    total = menu + bebida
    Iva = total * 0.08
    totalIva = total + Iva

    print(f"el valor total sin iva es de: ${total}")
    print(f"el valor total del IVA es de: ${Iva}")
    print(f"el valor total con inva incluido es de: {totalIva}")
elif opcional == "no":
    total = menu
    Iva = menu * 0.08
    totalIva = menu + Iva
    print(f"el valor total sin iva es de: ${total}")
    print(f"el valor total del IVA es de: ${Iva}")
    print(f"el valor total con inva incluido es de: {totalIva}")
else:
    print("la respuesta ingresada es incorrecta")