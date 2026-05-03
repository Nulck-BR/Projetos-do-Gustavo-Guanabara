primeiro = int(input("Digite o primeiro número: "))
razao = int(input("Digite a razão: "))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo, razao):
    print(i, end="-> ")
print("ACABOU")