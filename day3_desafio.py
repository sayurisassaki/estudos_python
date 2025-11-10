#Peça o nome de usuário e a senha. 
#Se o nome for "sayuri" e a senha "1234", exiba: "Login bem-sucedido"
#Caso contrário: "usuário ou senha incorretos."

login = input("Digite o nome de usuário: ")
senha = int(input("Digite sua senha: "))

if login == "sayuri" and senha == 1234:
    print("Login bem-sucedido!")
else: 
    print("Usuário ou senha incorretos")
    