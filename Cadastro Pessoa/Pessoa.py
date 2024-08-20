from datetime import date

class Endereco:
    def __init__(self, logradouro="", numero="", enderecoComercial=False):
        self.logradouro = logradouro
        self.numero = numero
        self.enderecoComercial = enderecoComercial


class Pessoa:
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco

    def calcularImposto(self, rendimento):
        return 

class PessoaFisica(Pessoa):
    def __init__(self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=""):
        if endereco is None:
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()
        
        super().__init__(nome, rendimento, endereco)

        self.cpf = cpf
        self.dataNascimento = dataNascimento

    def calcularImposto(self, rendimento: float) -> float:
        if rendimento <= 1500:
            return 0
        elif 1500 < rendimento <= 3500:
            return (rendimento / 100) * 2
        elif 3500 < rendimento <= 6000:
            return (rendimento / 100) * 3.5
        else:
            return (rendimento / 100) * 5

class PessoaJuridica(Pessoa):
    def __init__(self, nome="", rendimento=0.0, endereco=None, cnpj="", dataNascimento=""):
        if endereco is None:
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()

        super().__init__(nome, rendimento, endereco)

        self.cnpj = cnpj
        self.dataNascimento = dataNascimento

        def calcularImposto(self, rendimento: float) -> float:
            if rendimento <= 1500:
                return 0
            elif 1500 < rendimento <= 3500:
                return (rendimento / 100) * 2
            elif 3500 < rendimento <= 6000:
                return (rendimento / 100) * 3.5
            else:
                return (rendimento / 100) * 5