nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em maiúsculo ficará:", nome.upper())
print("Seu nome em minúsculo ficará:", nome.lower())
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
primeiro_nome = nome.split()[0]
print(f"Seu primeiro nome é '{primeiro_nome}' e tem {len(primeiro_nome)} letras")