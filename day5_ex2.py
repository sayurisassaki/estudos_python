#Peça ao usuário um número e exiba a tabuada dele (de 1 a 10):

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(numero * i)

    #outra forma de deixar o print mais apresentavel. 
    #print(f{numero} * {i} = {numero * i})