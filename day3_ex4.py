#Peça o salário do usuário: Se for maior que 5000 imprima salario alto
# entre 2500 e 5000 imprima salario médio e abaixo de 2500 salario baixo

salario = float(input("Digite o valor do seu salário: "))

if salario > 5000:
    print("Salário alto!")
elif salario <= 5000 and salario >= 2500:
    print("Salário médio!")
else:
    print("Salário baixo!")
