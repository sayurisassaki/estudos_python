#Crie um dicionário que represente um produto, contendo: nome, preço e disponivel(verdadeiro ou falso)
#depois imprima apenas o nome do produto e altere o calor de disponivel para falso.

produto = {
    "nome": "caneta",
    "preço": 2.00,
    "disponivel": True
}
print(produto["disponivel"])
produto["disponivel"] = False
print(produto["disponivel"])