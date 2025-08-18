from math import sin, cos, tan, radians
anglo = float(input("Digite o ânglo que voce deseja: "))
seno = sin(radians(anglo))
coseno = cos(radians(anglo))
tangente = tan(radians(anglo))
print(f"o anglo de {anglo} tem o seno de {seno:.2f}")
print(f"o anglo de {anglo} tem o coseno de {coseno:.2f}")
print(f"o anglo de {anglo} tem o tangente de {tangente:.2f}")