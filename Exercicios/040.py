n = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n + n2) / 2
print(f'tirando {n} e {n2} a média é {m}')


if 7 > m >= 5:
    print('O aluno está de recuperação')

elif m < 5:
    print('O aluno está reprovado')

elif m >= 7:
    print('O aluno está aprovado')