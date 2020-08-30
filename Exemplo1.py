#índice começa do 0
frutas = ["abacate","banana","cajá","limão","mamão","laranja","melancia"]

print(frutas)
print(frutas[1])
print(frutas[-1]) #de trás para frente. Print melancia
print(frutas[2:5]) #começando do elemento 2 até menor que 5. Print cajá, limão, mamão
print(frutas[:4]) #4 é exclusivo
print("**********")
frutas.append("ameixa")

for item in frutas:
    print(item, end=" / ")
print()
print("Quantidade de elementos: ", len(frutas))
print("Quantas vezes aparece banana na lista: ",frutas.count("banana"))

frutas.sort() # ordena os elementos da lista
print(frutas)

frutas.reverse() #inverte a ordem
print(frutas)

frutas.remove("cajá") #removeõ elemento "cajá"
print(frutas)

frutas.pop(4) #remove o elemento do índice 4
print(frutas)

frutas.insert(1,"seriguela")
print(frutas)

for fruta in frutas: #teste
    if fruta.startswith("m"):
        print(fruta)

print("Fruta: ", frutas[2])




