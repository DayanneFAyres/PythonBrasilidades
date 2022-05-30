from multiprocessing.sharedctypes import Value
from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def criaDocumento(documento):

        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

class DocCpf:
    def __init__(self, cpf):
        if self.valida(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF inválido!!")

    def __str__(self):
        return self.formata()

    def valida(self, cpf):
        validador = CPF()
        return validador.validate(cpf)
    
    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:

    def __init__(self, cnpj):
        if self.valida(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ inválido!!")

    def __str__(self):
        return self.formata()

    def valida(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)
    
    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)