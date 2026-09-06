a = 10
b = 3

resultado_and = (a>5) and (b<5) #true
resultado_or = (a> 15) or (b<5) #true
resultado_not = not (a>5) #False

# resultado dos operadores lógicos AND, OR e NOT
print("""Variaveis
a = 10
b =3""")
print(20*"__")
print(f"and(E) operação (a>5) and (b<5) = {resultado_and}")
print(f"or(OU) operação (a>15) and (b<5) = {resultado_or}")
print(f"not(negação) operação not (a>5) = {resultado_not}")
