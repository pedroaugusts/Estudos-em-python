import re

class Telefone:
    def __init__(self, telefone):
        self._telefone = self.__validar(telefone)

    def __regex(self,telefone):
        padrao = re.compile('[(]?[0-9]{2}?[)]?[0-9]{4}[-]?[0-9]{4}')
        busca = padrao.search(str(telefone))
        return busca

    def __validar(self, telefone):
        telefone = telefone
        busca = self.__regex(telefone)

        if busca:
            telefones = busca.group()
            return telefones
        else:
            raise ValueError("O número não esta no Padrão (xx)xxxx-xxxx")


    def __str__(self):
        format = str(self._telefone)
        return f"({format[0:2]}) {format[2:6]}-{format[6:10]}"
