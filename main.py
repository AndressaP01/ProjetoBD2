
from Crud import crud
from conta_bancaria import conta
from user import usuario
from database import Database
db = Database(database="BancoPROJETO2", collection="conta1")

user=usuario("Andressa","13277134556","SRS","37540000","MG",15000)
conta1=conta(user)
crud1=crud()
crud1.inserir("Andressa","13277134556","SRS","37540000","MG",15000)
crud1.buscar("Andressa")


















