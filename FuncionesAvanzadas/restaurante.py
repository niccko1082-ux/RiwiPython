total_cuenta = float(input("Ingresa el total de la cuenta: "))
def calcular_propina(total_cuenta):

    if total_cuenta >= 100000:
        propina = total_cuenta + (total_cuenta * 0.15)
        print(f"El valor total a pagar es: ${propina}")
    elif total_cuenta > 0:
        propina = total_cuenta + (total_cuenta * 0.10)
        print(f"El valor total a pagar es: ${propina}")
    else:
        print("error de dato ingresado")

calcular_propina(total_cuenta)
