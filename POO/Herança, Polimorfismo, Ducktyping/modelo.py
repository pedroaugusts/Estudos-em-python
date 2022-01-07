class Audiovisual:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    def darlike(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    #retorna um valor string do objetox'
    def __str__(self):
        return f" {self.nome} - {self.ano} - {self.likes} Likes"


class Filme(Audiovisual):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f" {self.nome} - {self.ano} - {self.duracao} Duração - {self.likes} Likes"



class Serie(Audiovisual):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f" {self.nome} - {self.ano} - {self.temporadas} Temporadas - {self.likes} Likes"

class Playlist:
    def __init__(self, nome, programas):
        self._programas = programas
        self.nome = nome

    #metodo que torna programas iteraveis
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)
