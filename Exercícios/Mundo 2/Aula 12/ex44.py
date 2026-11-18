preço_produto = float(input("Digite o preço do produto: R$ "))
pagamento = input("""
Digite a forma de pagamento (apenas o número correspondente):
1. Pagamento à vista
2. Pagamento à vista no cartão.
3. Pagamento parcelado.
""")
if pagamento == "1":
    desconto = preço_produto * 0.10
    preço_final = preço_produto - desconto
    print(f"Você recebeu um desconto de R$ {desconto:.2f}. O preço final é R$ {preço_final:.2f}.")
elif pagamento == "2":
    desconto = preço_produto * 0.05
    preço_final = preço_produto - desconto
    print(f"Você recebeu um desconto de R$ {desconto:.2f}. O preço final é R$ {preço_final:.2f}.")  
elif pagamento == "3":
    parcelas = int(input("Digite o número de parcelas (até 12): "))
    if parcelas <= 12:
        juros = preço_produto * 0.20
        preço_final = preço_produto + juros
        valor_parcela = preço_final / parcelas
        print(f"O preço final com juros é R$ {preço_final:.2f}. Cada parcela será de R$ {valor_parcela:.2f}.")
    else:
        print("Número de parcelas inválido. O máximo permitido é 12.")
else:
    print("Opção de pagamento inválida.")