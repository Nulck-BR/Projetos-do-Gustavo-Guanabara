from random import shuffle
p1 = str(input("Digite o primeiro aluno: "))
p2 = str(input("Digite o segundo aluno: "))
p3 = str(input("Digite o terceiro aluno: "))
p4 = str(input("Digite o quarto aluno: "))
lista = [p1, p2, p3, p4]
shuffle(lista)
print("a ordem de apresentaçao será")
print(lista)