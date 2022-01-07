class Cliente:

    def __init__(self,nome):
        self.__nome = nome

    #property transforma em uma propriedade, burla o uso dos parenteses do metodo
    @property
    def nome(self):
        #tornar a primeira letra do nome maiuscula
        return self.__nome.title()

    #adicionando um setter sem colocar set antes do nome 
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
