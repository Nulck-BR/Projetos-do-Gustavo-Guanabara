import random
import time
while True:
    print('Vou pensar em um número entre 0 e 5')

    sorteado = random.randint(0, 5)

    numero = int(input('Em qual número eu pensei? '))
    print('Processando...')
    time.sleep(1)

    if numero == sorteado:
        print('Você acertou!')
        break  # Sai do loop e encerra o programa

    elif numero < 0 or numero > 5:
        print('Digite um numero entre 0 a 5.')
        continue  # Volta ao início do loop

    else:
        print(f'Você errou! Eu pensei no número {sorteado}.')
        print("Vamos tentar de novo!")
        continue  # Volta ao início do loop