numero = int(input("Informe um número: "))
u = numero % 10
d = (numero // 10) % 10
c = (numero // 100) % 10
m = (numero // 1000) % 10
print(f"analisando o número {numero}")
#casas decimais
print(f"Unidade {u}")
print(f"Dezena {d}")
print(f"Centena {c}")
print(f"Milhar {m}")