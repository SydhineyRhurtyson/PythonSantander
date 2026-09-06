# if = Se
def idadeIF(idade):
    print(f"Idade: {idade}")
    if idade >= 18:
        print("Você é maior de idade")
# else = Se não
def idadeIFELSE(idade):
    print(f"Idade: {idade}")
    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")
# else = Se não se
def resultfinal(nota):
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

if __name__ == "__main__":
    idadeIF(18)
    print(40*"=")
    idadeIFELSE(15)
    print(40*"=")
    resultfinal(2)

