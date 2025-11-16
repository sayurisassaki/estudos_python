#Peça 5 número ao usuário (um por vez)
#Guarde todos os números em uma lista
#Mostre: A soma total dos números
#O maior número digitado
#O menor número digitado.
lista = []
numero1 = int(input("Digite o primeiro número: "))
lista.append(numero1)
numero2 = int(input("Digite o segundo número: "))
lista.append(numero2)
numero3 = int(input("Digite o terceiro número: "))
lista.append(numero3)
numero4 = int(input("Digite o quarto número: "))
lista.append(numero4)
numero5 = int(input("Digite o quinto número: "))
lista.append(numero5)

print("A soma dos números digitados é: ", sum(lista))
print("O maior número digitado foi: ", max(lista))
print("O menor número digitado foi: ", min(lista))
