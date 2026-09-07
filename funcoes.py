#função simples
def saudadcao(nome:str):
    print(f"Olá, {nome}")

#função com returno
def soma(a,b):
    return a + b


#função anonima
quadrado = lambda x: x ** 2
print(quadrado(3))

#diferençá de escopo das variaveis (Local vs global):
def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função


variavel_global = 20


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


# Imprime 20
# print(variavel_local)

#funções com arques *permiti colocar mais de uma arqgumento
def soma2(*n):
    r =0
    for valor in n:
        r += valor
    return r
def calcular_media(*notas):
    """"
    Args:
        *notas (float): notas do aluno para fazer a media, OBS pode ser quantas quiser
    Vai somar as notas do aluno e dividir pela quantidade de notas para fazer a media"""
    rsoma = soma2(*notas)
    quantidade = len(notas)
    media = (rsoma/quantidade)
    return round(media,3)
#Função recursiva onde a propria função chama ela mesma
def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero-1)

if __name__ == '__main__':
    # saudadcao("Ruth")
    # resultado = soma(3, 4)
    # print(resultado)
    #
    # funcao()  # Imprime 10
    # funcao2()  # Imprime 20
    # print(variavel_global)
    # print(calcular_media(7.5,6.9,8.4))
    print(fatorial(5))
