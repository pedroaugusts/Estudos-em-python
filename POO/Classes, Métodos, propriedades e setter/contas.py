# criação da classe conta
class Conta:
    # construtor da classe onde self é a referencia do obj na memoria
    def __init__(self, numero, nome, saldo, limite=1000.0):
        # atributos privados da classe
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        # função que mostra o extrato da conta na tela
        print("O saldo da conta de {} é: {}".format(self.__nome, self.__saldo))

    def depositar(self, valor):
        # deposito de um valor ao saldo
        self.__saldo += valor

    def __podesacar(self, valor):
        return valor <= (self.__saldo + self.__limite)

    def sacar(self, valor):
        # sacar um valor do saldo
        if self.__podesacar(valor):
            self.__saldo -= valor
        else:
            print("Você não tem limite para sacar esse valor de {} reais".format(valor))

    def tranferencia(self, obj2, valor):
        # transfer dinheiro de um obj da classe conta pra outro
        self.sacar(valor)
        obj2.depositar(valor)

    # funcoes get
    # o get é utilizado para buscar os valores
    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def nome(self):
        return self.__nome

    # metodo estatico, porém só faz sentido se todos os obj compartilharem algo em comum
    # porém, é necessário ter cautela a usar esses por se aproximarem da programação procedural
    @staticmethod
    def codigos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "247"}

    # outra maneira de criar um metodo set
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
