tecnica = 0.7
logica = 0.3

notaTecnica = float(input("Ingresa la nota Tecnica: "))
notaLogica = float(input("ingresa la nota Logica: "))

notaFinal = (notaTecnica*tecnica)+(notaLogica*logica)

if notaTecnica > 5.0 or notaTecnica < 0:
    print("error, ingresa una nota valida")
elif notaLogica > 5.0 or notaLogica< 0:
    print("error, ingresa una nota valida")
elif notaFinal >= 3.0:
    print(f"tu nota final es, {notaFinal} (Aprovado!)")
elif notaFinal < 3 and notaFinal >= 2:
    print(f"tu nota final es {notaFinal} (Revision)")
else:
    print(f"tu nota final es {notaFinal} (Reprovado)")

