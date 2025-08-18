nome = str(input("Digite seu nome completo: ")).strip().lower()
print(f'Muito prazer em te conhecer!')
print(f'seu primeiro nome é {nome.split()[0]}')
print(f'seu último nome é {nome.split()[-1]}')

# .split() é um método que divide uma string em uma lista de substrings com base em um delimitador (por padrão, espaços em branco).