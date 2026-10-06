num = int((input("Insira um número de 0 a 9999: ")))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"""
unidade: {u}  
dezena: {d}
centena: {c}
milhar: {m}
 """)