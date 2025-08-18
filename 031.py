distancia = float(input("Qual é a distância da sua viagem em km? "))
if distancia <= 200:
    print(f'Você está prestes a começar uma viagem de {distancia} km.')
    preco = distancia * 0.50
    print(f'O preço da sua passagem será de R$ {preco:.2f}.')

else:
    print(f'Você está prestes a começar uma viagem de {distancia} km.')
    preco = distancia * 0.45
    print(f'O preço da sua passagem será de R$ {preco:.2f}.')