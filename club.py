"""10. Club “Noche Estelar” — Acceso + validación documento
Pedir edad y documento.

Reglas:

Edad ≥ 18 → puede entrar solo si tiene documento.
Si la edad < 18 → "Entrada denegada"
Si tiene 18 o más pero no tiene documento →""" "Debe presentar documento"


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
    