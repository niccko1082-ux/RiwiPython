def aplicar_descuentos():
    conteo = 0
    while True:
        precio = float(input("Ingresa valor de compra: "))
        valor = precio - (precio * 0.10)
        if precio == 0:
            break
        elif precio >= 50000:
            conteo += valor 
            print(f"El valor total con descuento es de: ${conteo}")
        elif precio > 0:
            conteo += precio
            print(f"El valor total es de: ${conteo}")
        else:
            print("Error, ingresa un dato valido")

        
aplicar_descuentos()

    