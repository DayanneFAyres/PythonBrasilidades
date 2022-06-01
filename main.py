from acesso_cep import BuscaEndereco
import requests

cep = "01001000"
obj_cep = BuscaEndereco(cep)
print(obj_cep)
print(obj_cep.AcessaViaCep())