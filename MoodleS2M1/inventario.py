while True:
    menu = input("Ingresa la opcion que deseas: \n -Agregar productos \n -Mostrar Inventario \n -Calcular estadisticas \n -Salir \n\n")
    if menu.lower() != "Agregar productos" and menu.lower() != "Mostrar inventario" and menu.lower() != "Calcular estadisticas" and menu.lower() != "Salir":
        print("Ingresa una opcion valida \n")
    