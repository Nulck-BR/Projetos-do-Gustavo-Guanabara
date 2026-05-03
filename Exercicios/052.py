num = int(input("Digite um número: "))
for c in range(1, num + 1):
    if num % c == 0:
        print(f"\033[34m{c}\033[m", end=" ")
    else:
        print(f"\033[31m{c}\033[m", end=" ")
    print(c, end="")
    