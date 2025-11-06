edad = int(input("ingresa tu edad: "))

if edad >= 18:
    documento = input("Traes documento (Si/no)").lower()
else:
    print("Entrada denegada")
    exit()

if documento == "si":
    print("Puede entrar")
else:
    print("Puede entrar solo si tiene documento")
    