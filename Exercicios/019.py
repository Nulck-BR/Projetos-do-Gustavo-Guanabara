from random import choice
p1 = str(input("Digite o nome do primeiro aluno: "))
p2 = str(input("Digite o nome do segundo aluno: "))
p3 = str(input("Digite o nome do terceiro aluno: "))
p4 = str(input("Digite o nome do quarto aluno: "))
lista = [p1, p2, p3, p4]
print(f"o aluno escolhido foi {choice(lista)}")