ingresos = float(input("Ingresa total de ingresos mensuales: "))
edad = int(input("Ingresa tu edad: "))
def evaluar_credito(ingresos, edad):
    if ingresos >= 2000000 and edad > 24 and edad < 61:
        print("Credito aprobado")
    else:
        print("Credito rechazado")
    
evaluar_credito(ingresos, edad)