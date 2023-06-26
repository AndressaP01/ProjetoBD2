


class usuario:
    def __init__(self,nome,cpf,cidade,cep,estado,renda_mensal):
        self.nome=nome
        self.cpf=cpf
        self.cidade=cidade
        self.cep=cep
        self.estado=estado
        self.renda_mensal=renda_mensal
        from conta_bancaria import conta
        self.conta=conta



