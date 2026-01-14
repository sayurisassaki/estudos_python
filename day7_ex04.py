#Peça ao usuário para digitar quantos itens ele quiser. Continue pedindo até ele digitar "sair". Armazene tudo em uma lista

nomes = []

while True:
    nome = (input("Digite um nome ou 'sair' para encerrar: "))

    if nome.lower() == "sair":
        print("A lista foi encerrada! A lista possui ", len(nomes), "nomes")
        break
     
    nomes.append(nome)
