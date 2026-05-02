s1 = float(input("Digite o primeiro segmento: "))
s2 = float(input("Digite o segundo segmento: "))
s3 = float(input("Digite o terceiro segmento: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Os segmentos formam um triângulo.")
    if s1 == s2 == s3:
        print("O triângulo é equilátero.")
    elif s1 != s2 != s3 != s1:
        print("O triângulo é escaleno.")
    else:
        print("O triângulo é isósceles.")

else:
    print("Os segmentos não formam um triângulo.")