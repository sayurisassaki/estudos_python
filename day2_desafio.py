#Crie um programa que peça: 
#O nome do usuário
#Sua idade 
#Calcule em qual ano ele fará 100 anos.

from datetime import date
ano_atual = date.today().year

nome = input("Qual o seu nome? ")
idade = int(input("Quantos anos você tem? "))

ano = ano_atual + (100 - idade)
print(f"Seu nome é {nome} e você fará 100 anos em {ano}")

