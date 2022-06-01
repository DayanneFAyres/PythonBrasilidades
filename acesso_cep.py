import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)

        if self.ValidaCep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")
    def __str__(self):
        return self.FormataCep()

    def ValidaCep(self, cep):

        return len(cep) == 8
    
    def FormataCep(self):

        return "{}-{}".format(self.cep[:5], self.cep[5:])
    
    def AcessaViaCep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()

        return (
            dados.get("bairro"),
            dados.get("localidade"),
            dados.get("uf")
        )