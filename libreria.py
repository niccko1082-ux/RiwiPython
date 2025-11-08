libro = 25000
estudiante = 0.15
cupon = "LIBRO10"
descuentoCupon = 0.10

persona = input("eres estudiante(si/no): ").lower()
tlDescuento = input("ingresa el cupon: ")

if persona == "si" and tlDescuento == cupon:
    valor = libro - (libro * estudiante)
    valor = valor - (valor * descuentoCupon)
    print(f"el valor total del libro es de: ${valor}")

elif persona == "si" and tlDescuento != cupon:
    valor = libro - (libro * estudiante)    
    print(f"el valor total del libro es de: ${valor}")
else:
    print("El cupon no aplica")
    print(f"el valor total es del libro es de: ${libro}")