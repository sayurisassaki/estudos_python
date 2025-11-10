#Peça o ano de nascimento e informe se a pessoa é menor de idade ou maior de idade.

from datetime import date 

ano_atual = date.today().year
nasc = int(input("Digite seu ano de nascimento: "))

ano = ano_atual - nasc

if ano > 18:
    print("Você é maior de idade ")
else: 
    print("Você é menor de idade")