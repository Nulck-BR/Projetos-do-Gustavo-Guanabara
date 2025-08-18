primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))
terceiro_valor = int(input("Digite o terceiro valor: "))

menor_valor = min(primeiro_valor, segundo_valor, terceiro_valor)
maior_valor = max(primeiro_valor, segundo_valor, terceiro_valor)
#min serve para encontrar o menor valor entre os números
#max serve para encontrar o maior valor entre os números

print(f'o menor valor: {menor_valor}')
print(f'o maior valor: {maior_valor}')
