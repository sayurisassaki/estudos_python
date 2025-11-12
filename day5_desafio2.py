#Peça ao usuário um número inteiro positivo
#Conte de 1 até esse número. 
#Para cada número: 
    #Se for multiplo de 3, exiba a palavra "fizz"
    #Se for multiplo de 5, exiba a palabra "buzz"
    #Se for multiplo de 3 e 5 ao mesmo tempo, "FizzBuzz"
    #Caso contrário, apenas mostre o próprio número.
#Ao final, mostre a mensagem: "Contagem finalizada!"

numero = int(input("Digite um número inteiro positivo: "))
for i in range(1, numero +1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("Contagem finalizada!")