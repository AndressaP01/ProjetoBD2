class SimpleCLI:
    def __init__(self):
        self.commands={}
    def add_command(self,name,function):
        self.commands[name]=function
    def run(self):
        while True:
            command=input("Entre com um comando: ")
            if command=="quit":
                print("Godbye")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command")

class PersonCLI(SimpleCLI):
    def __init__(self,Database):
        super().__init__()
        self.Database=Database
        self.add_command("create",self.create)
        self.add_command("read",self.read)
        self.add_command("update", self.update)
        self.add_command("delete", self.delete)

    def create(self):
        nome=input("Entre com o nome: ")
        cpf = input("Entre com o cpf: ")
        cidade = input("Entre com o nome de sua cidade: ")
        cep = input("Entre com o cep: ")
        estado = input("Entre com o estado: ")
        renda = input("Entre com a renda: ")
        self.Database.create(nome,cpf,cidade,cep,estado,renda)



    def update(self):
        nome=input("Entre com nome: ")
        cidade = input("Entre com o nome de sua cidade: ")
        cep = input("Entre com o cep: ")
        estado = input("Entre com o estado: ")
        renda = input("Entre com a renda: ")
        self.Database.update(id,nome,cidade,cep,estado,renda)

    def delete(self):
        nome=input("Entre com o nome: ")
        self.Database.delete(nome)

    def run(self):
        print("Welcome to the person CLI!")
        print("Available commands: create, read,update,delete,quit")
        super().run()

