# arquivo = open("dados.txt", "r")
# conteudos = arquivo.read()
# for conteudo in conteudos:
#     print(conteudo)
#     print("="*40)
# arquivo.close()

def imprimir_count(diretorio:str):
    with open(diretorio, "r") as arquivo:
        conteudos = arquivo.readlines()
        for conteudo in conteudos:
            print(conteudo)

if __name__ == '__main__':
    imprimir_count("dados.txt")

