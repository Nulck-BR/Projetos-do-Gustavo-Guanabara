n = int(input('Digite um número: '))
print("Escolha uma conversão: ")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{n} convertido para binário é {bin(n)[2:]}')
elif opção == 2:
    print(f'{n} convertido para octal é {oct(n)[2:]}')
elif opção == 3:
    print(f'{n} convertido para hexadecimal é {hex(n)[2:]}')
else:
    print('Opção inválida!')