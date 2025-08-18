frase = str(input("Digite uma frase: ")).strip().lower()
print(f"A letra 'a' aparece {frase.count('a')} vezes.")
print(f"A primeira letra 'a' aparece na posição {frase.find('a')}.")
print(f"A última letra 'a' aparece na posição {frase.rfind('a')}.")

#find é para encontrar a primeira aparicao do caractere
#rfind é para encontrar a última aparicao do caractere