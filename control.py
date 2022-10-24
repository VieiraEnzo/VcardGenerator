class Usuario:
    def __init__(self, login, nome_completo, senha,id):
        self.login = login
        self.nome_completo = nome_completo
        self.senha = senha


class Cartao:
    def __init__(self, nome,telefone,site,email,end): 
        self.nome = nome
        self.telefone = telefone
        self.site = site
        self.email = email
        self.end = end
