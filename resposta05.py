pares = []
impares = []

for numero in range(11):
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Pares: ", pares)
print("Impares: " , impares)