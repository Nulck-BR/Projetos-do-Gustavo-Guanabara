import math

# 1. Funções básicas de entrada e saída
nome = input("Qual seu nome? ")
print("Olá,", nome)

# 2. Tipos de dados
inteiro = 10
flutuante = 3.14
texto = "Python"
booleano = True

# 3. Operações matemáticas
soma = 2 + 3
multiplicacao = 4 * 5
divisao = 10 / 2
resto = 7 % 3

# 4. Estruturas de decisão
if inteiro > 5:
    print("Maior que 5")
else:
    print("Menor ou igual a 5")

# 5. Estruturas de repetição
for i in range(5):
    print("Contando:", i)

contador = 0
while contador < 3:
    print("While:", contador)
    contador += 1

# 6. Listas e manipulação
lista = [1, 2, 3]
lista.append(4)
print(lista)
for item in lista:
    print(item)

# 7. Funções
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))

# 8. Dicionários
dicionario = {"nome": "João", "idade": 25}
print(dicionario["nome"])

# 9. Manipulação de strings
texto = "Python é legal"
print(texto.upper())
print(texto.replace("legal", "incrível"))

# 10. Manipulação de arquivos
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Aprendendo Python!")

# 11. Importação de módulos
print(math.sqrt(16))

# 12. List comprehensions
quadrados = [x**2 for x in range(5)]
print(quadrados)