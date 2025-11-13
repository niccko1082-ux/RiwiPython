"""print("1. enero")
print("2. febrero")
print("3. marzo")
print("4. abril")
print("5. mayo")
print("6. junio")

total = 0

for i in range(6):
    ahorro = int(input("Ingresa la cantidad que deseas ahorar: "))
    total += ahorro
    mes = 0
    if total != 1000000:
        mes += 1
        print(f" el mes es: {mes}")
    else:
        print("Meta alcanzada!")"""

print("1. enero")
print("2. febrero")
print("3. marzo")
print("4. abril")
print("5. mayo")
print("6. junio")

total = 0  # acumulador general

for i in range(6):
    ahorro = int(input(f"Ingrese la cantidad que deseas ahorrar en el mes {i + 1}: "))
    total += ahorro  # sumamos el ahorro de este mes al total acumulado

    if total >= 1000000:
        print(f"¡Meta alcanzada en el mes {i + 1}!")
        break  # si ya llegamos a la meta, detenemos el ciclo
    else:
        print(f"Total acumulado hasta ahora: ${total:,}")

# Mostrar total final
print(f"\nAhorro total acumulado: ${total:,}")
