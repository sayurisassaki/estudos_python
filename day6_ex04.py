#Dada uma lista vazia, adicione três nomes, converta para uma tupla e mostre a tupla resultante. 
lista = []

for i in range(3):
    lista.append(input("Digite um nome: "))

tupla = tuple(lista)
print(tupla)