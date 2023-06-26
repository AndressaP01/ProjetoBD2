
class crud:
    def inserir(self,nome,cpf,cidade,cep,estado,renda):
        from main import db
        db.collection.insert_one({"nome": nome, "cpf":cpf, "cidade":cidade,"cep":cep,"estado":estado,"renda":renda})


    def deletar(self,nome):
        from main import db
        db.collection.delete_one({"nome":nome})

    def update(self,nome,cidade,cep,estado,renda):
        from main import db
        db.collection.update_one({"nome":nome}, {"$set": {"nome":nome, "cidade":cidade,"cep":cep,"estado":estado,"renda":renda}})

    def buscar(self,nome):
        from main import db
        print(db.collection.find_one({"nome":nome}))





