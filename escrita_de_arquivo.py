
# arquivo= open(diretorio,"w")
# arquivo.write("Ola mundo")
# arquivo.close()

def escrita_arquivo(direct:str,*dados:str):
    with open(direct, mode='w') as arquivo:
        for dado in dados:
            arquivo.write(dado+'\r')


if __name__ == '__main__':
    diretorio = "dados_do_user.txt"
    nome = str(input("Digite o seu nome: "))
    idade = str(input("Digite a sua idade: "))
    escolaridade = str(input("Digite a sua escolidade: "))
    textinho = str(input("Digite um textinho que te descreva: "))
    escrita_arquivo(diretorio,nome,idade,escolaridade,textinho)
    from leitura_de_arquivo import imprimir_count
    imprimir_count(diretorio)