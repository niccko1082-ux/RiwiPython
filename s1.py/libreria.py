"""5. Librería “El Saber” — Descuento estudiante + cupón
Libro cuesta $25.000.

Si es estudiante → 15% descuento
Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado
Validar:

Si no es estudiante, el cupón no aplica.
Si ingresa cupón incorrecto, ignorarlo.
Mostrar total."""


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