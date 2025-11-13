user = int(input("INGRESE UNA CANTIDAD: "))
count = 0

for i in range(user):
    count += 1
    if count % 2 == 0:
        print("Poducto verificado")
    else:
        print("Produnto pendiente")

