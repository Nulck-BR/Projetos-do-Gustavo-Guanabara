from random import randint
itens = ("pedra", "papel", "tesoura")
computador = randint(0, 2)

print("suas opções: ")
print("1 - pedra")
print("2 - papel")   
print("3 - tesoura")

jogada = int(input("Qual é a sua jogada? "))

print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogada - 1]}")

if computador == 0: # computador jogou pedra
    if jogada == 1:
        print("EMPATE")
    elif jogada == 2:
        print("JOGADOR VENCE")
    elif jogada == 3:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 1: # computador jogou papel
    if jogada == 1:
        print("COMPUTADOR VENCE")
    elif jogada == 2:
        print("EMPATE")
    elif jogada == 3:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 2: # computador jogou tesoura
    if jogada == 1:
        print("JOGADOR VENCE")
    elif jogada == 2:
        print("COMPUTADOR VENCE")
    elif jogada == 3:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")