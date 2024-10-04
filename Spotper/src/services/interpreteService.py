# pylint: disable=all
import logging
from src.database.database import DatabaseService
from src.entidades.interprete import Interprete
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class InterpreteService:
    def __init__(self):
        pass
    
    def add_to_db(self):
        interprete=Interprete()
        sql_query="INSERT INTO interprete (nome,tipo) VALUES (%s,%s)"
        params=(interprete.nome,interprete.tipo)
        DatabaseService().insert(sql_query,params)
        
    def view_all_interpretes(self):
        sql_query="SELECT nome,tipo FROM interprete"
        interpretes=DatabaseService().search(sql_query)
        print("--------INTERPRETES---------")
        for interprete in interpretes:
            print(interprete["nome"], interprete["tipo"])
        
    def search_by_name(self, nome):
        sql_query = "SELECT nome FROM interprete WHERE nome = %s"
        params = (nome,)  
        result = DatabaseService().search(sql_query, params)

        if result:
            print(result[0]['nome'])
            return result[0]['nome']
        
        logger.error(f"Nenhum intérprete de nome '{nome}' encontrado")
        
    def delete_by_name(self,nome):
        sql_query="delete from interprete where nome = %s"
        params=(nome,)
        DatabaseService().delete(sql_query,params)
        
        
        

        
  
        
        

