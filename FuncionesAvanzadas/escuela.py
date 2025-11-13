def promedio_notas():
    contador = 0
    for i in range(3):
        i += 1
        notas = float(input(f"Ingresa la nota {i}: "))
        contador += notas
        promedio = contador / 3
    if promedio >= 3.0:
        print(f"Aprovado! la nota final es: {promedio}")
    else:
        print(f"Reprovado!, la nota final es: {promedio}")
    
promedio_notas()