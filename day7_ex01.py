#Crie uma lista com 5 nomes e exiba:
#O primeiro item, o último item e o tamanho da lista

lista = []
for i in range (5):
    lista.append(input(f"Digite um nome {i+1}: "))

print(lista[0])
print(lista[-1])
print(len(lista))