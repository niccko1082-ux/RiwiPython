customer = 0

for i in range(8):
    customer += 1
    if customer != 8:
        print(f"atendiendo cliente numero {customer}")
    else:
        print("Ultimo cliente del dia")
        