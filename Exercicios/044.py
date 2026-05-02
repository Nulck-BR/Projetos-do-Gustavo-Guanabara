preço = float(input("Digite o preço das compras : R$"))
print(f"Valor a pagar: R${preço:.2f}")
print("Formas de pagamento:")
print("1 - À vista dinheiro/cheque: 10% de desconto")
print("2 - À vista cartão: 5% de desconto")
print("3 - Em até 2x no cartão: preço normal")
print("4 - 3x ou mais no cartão: 20% de juros")

opção = int(input("Escolha a forma de pagamento (1-4): "))

if opção == 1:
    valor_final = preço * 0.9
elif opção == 2:
    valor_final = preço * 0.95
elif opção == 3:
    valor_final = preço
elif opção == 4:
    valor_final = preço * 1.2
else:    
    print("Opção inválida.")
    valor_final = preço

print(f"Valor final a pagar: R${valor_final:.2f}")