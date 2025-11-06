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