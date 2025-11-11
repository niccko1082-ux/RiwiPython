array = [2,3,4,5,1,8,150]

suma = 0

for item in array:
    suma = suma + item
print(suma)

array.sort()
suma_minima = sum(array)
print(array)

array.sort(reverse=True)
suma_maxima = sum(array)
print(array)

print(f"suma de minima: {suma_minima}")
print(f"suma de maxima: {suma_maxima}")



