#Crie uma lista chamada animais com 3 nomes de animais e exiba o segundo.
#Adicione um novo animal ao final da listas
#Remova o primeiro animal
#mostre quantos itens há na lista
#ordene por ordm alfabética
animais=["cachorro", "gato", "leão"]
print("Segundo animal da lista: ", animais[1])
animais.append("cobra")
print("Depois de adicionar um novo animal: ", animais)
animais.remove(animais[0])
print("Depois de remover o primeiro animal: ", animais)
print("Quantidade de animais na lista: ", len(animais))
animais.sort()
print("Lista organizada em ordem alfabética: ", animais)
