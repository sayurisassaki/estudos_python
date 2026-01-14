#Crie um dicionário que represente um evento, contendo: nome do evento, conjunto de participantes(nomes)
#Depois: adicione novos participantes, tente adicionar um participante repetido, imprima os participantes do evento
evento = {
    "nome" : "Up!ABC",
    "participante" : set()

        
}
evento["participante"].add("Thiago")
evento["participante"].add("Sayuri")
evento["participante"].add("Thiago")
print(evento)
