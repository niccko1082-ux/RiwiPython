print("Viaje corto (< 1000 km): 500 millas")
print("Medio (1000–3000 km): 1000 millas")
print("Largo (> 3000 km): 2000 millas")
print("Ingresa 'fin' para finalizar.\n")

def calcular_millas(viajes):
    total_millas = 0
    for i in range(viajes):
        distancia = input(f"Viaje {i + 1}: Ingresa la cantidad de kilómetros (o 'fin'): ")

        if distancia.lower() == "fin":
            break  # Sale del bucle si el usuario termina antes

        try:
            km = float(distancia)

            if km < 0:
                print("❌ Ingresa una cantidad válida (no negativa).")
                continue
            elif km < 1000:
                total_millas += 500
            elif km <= 3000:
                total_millas += 1000
            else:
                total_millas += 2000

        except ValueError:
            print("⚠️ Ingresa un número válido o 'fin' para salir.")

    print(f"\n✈️ Total de millas acumuladas: {total_millas}")

# Programa principal
viajes = int(input("Ingresa el total de viajes planeados: "))
calcular_millas(viajes)

        
        