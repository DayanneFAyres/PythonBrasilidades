from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def __str__(self):
        return self.formata_cpf()

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("CPF não tem 11 dígitos.")  

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)