nascimento = int(input('Digite um ano: '))
atual = 2026
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
if idade == 18:
    saldo = 18 - idade
    print(f'Você tem que se alistar IMEDIATAMENTE! Falta apenas {saldo} ano para o alistamento!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento!')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos!')
else:
    print('Valor inválido!')