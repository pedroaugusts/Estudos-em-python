from cpf import Documento
from telefone import Telefone
import requests

from cep import BuscaEndereco

cpf_um = "15316264754"

documento = Documento.cria_documento(cpf_um)
print(documento)

celular = Telefone(2191584831)
print(celular)


cep = "25800320"
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)
