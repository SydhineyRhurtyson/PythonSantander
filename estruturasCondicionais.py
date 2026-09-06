# if = Se
idade = 18
print(f"Idade: {idade}")
if idade >= 18:
    print("Você é maior de idade")
# elif = Se não se
print(20*"__")
idade = 15
print(f"Idade: {idade}")
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
# else = Se não
print(20*"__")
nota = 8.5
print(f"Nota: {nota}")
resut = "Aprovado"
if nota >= 9:
    print("Exelente")
elif nota >= 8:
    print("muito bom")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Precisa Melhorar")
    resut = "Recuperação"
else:
    print("Infelizmente não foi dessa vez")
    resut = "Reprovado"

print(resut)


