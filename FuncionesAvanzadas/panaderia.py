lotes =  int(input("Ingresa la cantidad de lotes: ")) 
def hornear_pan(lotes):
    for i in range(lotes):
        i += 1
        print(f"El lote que se esta horneando es: {i}")
        if i % 3 == 0:
            print("Verificacion de calidad")
            
    print("Produccion terminda")

hornear_pan(lotes)