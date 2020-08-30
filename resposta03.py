notas = []
soma = 0

for i in range (1,5):
    nota = float(input(f"Digite a nota{1}: "))
    soma += nota
    notas.append(nota)

media = soma / 4

for i in range(4):
    print(f"Nota {i} = ",notas[i])

print("Média = ",media)