
#(a_n = a_{1} + (n-1) * r
a1 = int(input(f"Insira o primeiro termo da PA: "))
r = int(input(f"Insira a razão da PA: "))
for num in range (1, 11):
    an = a1 + (num - 1) * r
print(f"{f'Os 10 primeiros termos da PA':=^40}")
for num in range (1, 11):
    an = a1 + (num - 1) * r
    print(an)