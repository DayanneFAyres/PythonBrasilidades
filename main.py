from cpf_cnpj import Documento


exemplo_cnpj = "35379838000112"
exemplo_cpf = "74131294001"

documento = Documento.criaDocumento(exemplo_cpf)
print(documento)