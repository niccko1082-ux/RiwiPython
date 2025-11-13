def calcularInteres():
    monto = int(input("Ingresa el monto a invertir: "))
    tasa = float(input("Ingresa la tasa que deseas: "))
    time = int(input("Ingresa la cantidad de meses que deseas invertir: "))
    porcentaje = monto * (tasa / 100)
    ganancia = porcentaje * time

    print(f"la inversion tornara en {time} meses un total de ${ganancia}")
    return
calcularInteres()


