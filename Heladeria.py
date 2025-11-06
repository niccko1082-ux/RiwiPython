helado = input("elige un sabor de helado (chocolate/vainilla)").lower()

if helado == "chocolate":
    valor = 4000
elif helado == "vainilla":
    valor = 3500
else:
    print("Sabor no disponible")
    exit()
    
topping = input("Desea agregar el topping (si/no)").lower()
valorTopping = 1000

if topping == "si":
    valor_total = valor + valorTopping
    print(f"El valor total del helado: {valor_total}")
else:
    print(f"El valor del helado es: ${valor}")