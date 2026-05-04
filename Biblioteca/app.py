# Sistema de biblioteca console
class Livro:
    def __init__(self, titulo, autor, ano):  #self é uma referência ao objeto atual, chama a classe para criar um objeto.
        #privar os dados
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano


    #getter -> Permite acessar o título
    @property
    def titulo(self):
        return self.__titulo
    
    #setter -> Permite alterar o conteúdo

    @titulo.setter
    def titulo(self, novo_titulo):
        if len(novo_titulo) < 2:
            print("Título muito curto")
        else:
            self.__titulo = novo_titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, novo_autor):
        if len(novo_autor) < 2:
            print("Nome do autor muito curto")
        else:
            self.__autor = novo_autor

    @property
    def ano(self):
        return self.__ano
    
    ano.setter
    def ano(self, novo_ano):
        if not novo_ano.isdigit() or int(novo_ano) < 4:
            print("Ano inválido")
        else:
            self.__ano = novo_ano




    def exibir (self):
        print("Título: ", self.titulo)
        print("Autor: ", self.autor)



livros = []
    
while True:
    print("\n ==== Sistema de Biblioteca ====")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano de publicação: ")
        
        livro = Livro(titulo, autor, ano)
       # livros.append(livro)
        

        arquivo = open("livros.txt", "a")
        arquivo.write(livro.titulo + " - "+ livro.autor + " - "+ ano +" \n")
        arquivo.close()
        
        print(livros)

    elif opcao == "2":
        arquivo = open("livros.txt", "r")
        livros = arquivo.readlines()
        print("\n ==== Livros Cadastrados ====")
        for livro in livros:
            print(livro.strip())
            #print(livro.exibir())
        
        
        arquivo.close()

    
    elif opcao == "3":
        print("Saindo do sistema. Até logo!")
        break