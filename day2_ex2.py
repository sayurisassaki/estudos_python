n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

print(f"A soma é {n1+n2}, a média é {(n1+n2)/2}")

if n1 > n2:
    print(f"O maior número é:{n1} ")
elif n2 > n1:
    print(f"O maior número é: {n2}")
else: 
    print(f"Os dois números são iguais.")

