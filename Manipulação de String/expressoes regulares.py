#biblioteca de expressões regulares
import re
endereco = "Rua das flores, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)
else:
    raise ValueError("Nenhum CEP foi encontrado")


padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
string = "https://www.bytebank.com.br/cambio"
match = padrao_url.match(string)

if match:
    print("A URL é válida")
else:
    raise ValueError(" A url não é valida")
