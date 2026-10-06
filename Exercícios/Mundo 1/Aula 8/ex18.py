import math
ang = float(input("Insira um ângulo: "))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f"""
A Partir do Ângulo {ang}° temos:
Seno = {sen:.4f}
Cosseno = {cos:.4f}
Tangente = {tan:.4f}
      """)