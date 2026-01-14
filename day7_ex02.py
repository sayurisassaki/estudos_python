#Peça para um usuário digitar 3 números e armazene em uma lista. Depois calcule a soma desses números.

lista = []
for i in range (3):
    lista.append(int(input("Digite um número: ")))

print("A soma dos números digitados é: ", sum(lista))

