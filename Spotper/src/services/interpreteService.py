from database.database import DatabaseService
from entidades.interprete import Interprete

class InterpreteService:
    def __init__(self):
        pass
    
    def add_to_db(self):
        interprete=Interprete()
        sql_query="INSERT INTO interprete values(nome,tipo) VALUES (%s,%s)"
        params=(interprete.nome,interprete.tipo)
        DatabaseService().insert(sql_query,params)
        

