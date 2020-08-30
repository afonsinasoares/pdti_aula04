vet=[]
for n in range(1,11):
    num = int(input(f"Informe os números {n}: "))
    vet.append(num)
vet.sort(reverse=True)
print(vet)