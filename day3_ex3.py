#Peça dois números e diga qual é o maior.
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num1 > num2: 
    print(f"O número {num1} é o maior número digitado.")
elif num2 > num1: 
    print(f"O número {num2} é o maior número digitado.")
else: 
    print("Os números digitados são iguais.")