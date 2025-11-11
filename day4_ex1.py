#Faça um programa que peça uma senha ao usuário. 
#Ele deve continuar pedindo enquanto a senha estiver errada
#Quando o usuário digitar a senha correta, o programa deve apresentar "acesso permitido" e para.

senha = 0

while senha != 1234:
    senha = int(input("Digite sua senha: "))

print("Acesso permitido!")