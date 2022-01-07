class Jogo:
    def __init__(self):
        self._tabuleiro = Tabuleiro()
        self._turno = True

    def mover(self, daqui, prala):
        pass




class Tabuleiro:
    def __init__(self):
        self._tabuleiro = []

    def _createtable(self):
        for i in range(8):
            self._tabuleiro.append([None] * 8)

    def _imprimir(self):
        pass

    def __str__(self):
        return f"{self._tabuleiro}"



class peca:
    def __init__(self,cor):
        self._nome = ""
        self._cor = cor

    pass


class peao(peca):
    def __init__(self,cor):
        super().__init__(cor)
        self._nome = "P"

    def movimento(self):
        pass


class Cavaleiro(peca):
    def __init__(self,cor):
        super().__init__(cor)
        self._nome = "C"

    def movimento(self):
        pass


class Rainha(peca):
    def __init__(self,cor):
        super().__init__(cor)
        self._nome = "R"

    def movimento(self):
        pass


class Bispo(peca):
    def __init__(self,cor):
        super().__init__(cor)
        self._nome = "B"

    def movimento(self):
        pass


class Torre(peca):
    def __init__(self,cor):
        super().__init__(cor)
        self._nome = "T"

    def movimento(self):
        pass


class Rei(peca):
    def __init__(self,cor):
        super().__init__(cor)
        self._nome = "K"

    def movimento(self):
        pass
