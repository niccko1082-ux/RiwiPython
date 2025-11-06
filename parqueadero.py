hora = 2000
multa = 5000
cantHoras = int(input("ingresa la cantidad de horas de parqueadero: "))

if cantHoras < 0:
    print("error")
elif cantHoras < 5:
    hora = hora * cantHoras
    print(f"La cantidad de horas son: {cantHoras}h")
    print(f"valor total a pagar es de: ${hora}")
else:
    hora = hora * cantHoras + multa
    print(f"La cantidad de horas son: {cantHoras}h")
    print(f"el valor total a pagar es de {hora}")