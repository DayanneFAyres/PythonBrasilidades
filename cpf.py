class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueErrror("CPF inválido!!")

    def __str__(self):
        return self.formata_cpf()

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def formata_cpf(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        cpf_formatado = '{}.{}.{}-{}'.format(
            fatia_um,
            fatia_dois,
            fatia_tres,
            fatia_quatro
        )

        return cpf_formatado