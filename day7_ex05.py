#Remova todas as ocorrencias de número 2 da lista [1, 2, 3, 2, 4, 2, 5].

lista = [1, 2, 3, 2, 4, 2, 5]
nova_lista = []
print(lista)


for i in lista:
    if i != 2:
    lista.remove(2)

print(nova_lista)