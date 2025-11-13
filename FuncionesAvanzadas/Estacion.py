pasajeros = 10
def simular_viaje(pasajeros):
    for i in range(pasajeros):
        i += 1
        if i != 10:
            print(f"pasajero {i} a bordo")
        else:
            print(f"Bus lleno")
        
simular_viaje(pasajeros)