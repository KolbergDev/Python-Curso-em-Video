produto = float(input("Insira o valor do produto (R$): "))
desconto = produto * 0.05
preço_final = produto - desconto
print(f"Parabéns, você ganhou 5% de desconto de primeira compra, você ira pagar R${preço_final :.2f}.")