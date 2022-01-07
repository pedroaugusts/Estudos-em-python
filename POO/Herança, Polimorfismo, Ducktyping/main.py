from modelo import Audiovisual, Filme, Serie, Playlist

capfantastico = Filme("Capitão Fantástico", 2017, 120)

sexeduc = Serie("Sex Education", 2019, 3)
spiderman = Filme("Homem-Aranha", 2021, 180)
tvd = Serie("the vampire diares", 2012, 10)

lista = [capfantastico, sexeduc, spiderman,tvd]

passatempo = Playlist('passatempo', lista)

print(len(passatempo))
