def agregar_plato(menu, plato):
    plato = plato.strip()

    if plato == "":
        print("Ingresa un dato no vacio")
        return
    
    if plato in menu:
        print("Plato duplicado")
    else:
        menu.append(plato)
        print(f"{plato} agregado al menu")

def correr_menu():
    
    print("ingresa 'fin' para terminar")

    menu = []
    while True:
        plato = input("\nIngresa el nombre del plato: ").lower()
        if plato == ("fin"):
            break
        
        agregar_plato(menu, plato)

    for i, p in enumerate(menu, start=1):
        print(f"{i}. {p}")
    print(f"\nTotal de platos del menu: {len(menu)}")

correr_menu()

