#Erro de sintaxe(SyntaxError)
# def minha_funcao() # Faltam os dois pontos
#     print("Olá")

#Erro de nome(NameError)
# print(variavel_nao_definida)

#Erro de tipo (TypeError)
# resultado = 5+"10"

# #Erro de índice(IndexError)
# lista =[3,2,1]
# print(lista[3])

#manejo de exceções

#try
# try :
#     print(10/"1")
# #excepet
# except ZeroDivisionError :
#     print("Erro: dividido por zero")
# except ValueError :
#     print("Erro: valor invalido")
# except TypeError  :
#     print("Erro: tipo invalido")

# finally
# try:
#     arquivo = open("arquivo.txt", "r")
#     arquivo.write("Olá, Mundo")
# except FileNotFoundError:
#     print("Erro : arquivo não encotrado")
# finally:
#     arquivo.close()
#erro personalizado
def funcao():
    # Código que pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro")


try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")