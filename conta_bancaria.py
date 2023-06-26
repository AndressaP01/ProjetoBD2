from user import usuario


class conta:
    def __init__(self,usuario):
        self.usuario=usuario



    def listar_dados(self):
        print(self.usuario.nome)
        print(self.usuario.cpf)
        print(self.usuario.cidade)
        print(self.usuario.estado)
        print(self.usuario.renda_mensal)


    def tipo_de_conta(self):
        res=input("Escolha o tipo de conta, digite 2 para conta corrente e 3 para conta poupança:")
        if res==1:
          print("Você escolheu conta corrente")
        else:
          print("Você escolheu conta poupança")
        pass




    def cartao_de_credito(self):
        res=input("Você deseja cartão de credito?Digite sim ou não")
        if res=='sim':
            print("Cartão de crédito adicionado na conta")
        elif res=='nao':
            print("cartão de crédito não será adicionado na conta")
        pass


    def limite_conta(self):
        res=input("Você deseja adicionar limite na conta? Digite sim ou não")
        if res=='sim':
            print("Limite adicionado em sua conta ")
        elif res=='nao':
            print("Limite não foi adicionado na conta")
        pass





