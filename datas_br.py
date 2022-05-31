from datetime import datetime

class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def MesCadastro(self):
        meses = {
            1:"janeiro",          2:"fevereiro",
            3:"março",            4:"abril",
            5:"maio",             6:"junho",
            7:"julho",            8:"agosto",
            9:"setembro",         10:"outubro",
            11:"novembro",        12:"dezembro"
        }

        mes_cadastro = self.momento_cadastro.month

        return meses.get(mes_cadastro)

    def DiaSemanaCadastro(self):

        dias_semana = {
            1:"segunda",    2:"terça",
            3:"quarta",     4:"quinta",
            5:"sexta"
        }

        dia_semana_cadastro = self.momento_cadastro.weekday()

        return dias_semana.get(dia_semana_cadastro)
