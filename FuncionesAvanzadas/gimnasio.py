
num = int(input("Ingresa las cantidad de repeticiones"))
def repeticiones(n):
    

    for rep in range(n):
        if rep % 2 == 0:
            print(f"Excelente forma")
        else:
            print("Manten el ritmo!")
    return n
repeticiones(num)