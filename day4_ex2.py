#Peça o valor de uma compra e: 
#se for maior que 100, aplique 10% de desconto
#se for entre 50 e 100, aplique 5%
#caso contrário, sem desconto 

produto = float(input("Digite o valor do produto: R$ "))

if produto > 100:
    desc10 = produto - (produto*0.10)
    print(f"O valor do produto ficou R${desc10}. Você recebeu 10% de desconto")
elif produto >= 50 and produto <= 100:
    desc5 = produto - (produto*0.05)
    print(f"O valor do produto ficou R${desc5}. Você recebeu 5% de desconto")
else:
    print("Você não recebeu desconto!")
