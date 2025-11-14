''') Teatro “Butacas VIP” — Insertar reserva en posición
Como encargado de reservas, quiero una función insertar_reserva(butacas, nombre, posicion) que valide que posicion esté en rango y ubique la reserva en esa posición.

Si la posición no es válida, no inserta y muestra error.
Luego, recorre la lista para confirmar el orden.
Sugerencia: usa list.insert().'''
def insertar_reserva(butacas, nombre, posicion):
    
    nombre = nombre.strip()

    if nombre == "":
        print("El nombre no puede estar vacio")
        return
    
    if posicion < 0 and posicion > len(butacas):
        print(f"posicion invalida, el rango valido de 0 a {len(butacas)}")
        return
    
    butacas.insert(posicion, nombre)

