# pylint: disable=all
import logging
from database.database import DatabaseService
from entidades.interprete import Interprete
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
        sql_query="SELECT * FROM interprete"
        interpretes=DatabaseService().search(sql_query)
        print("--------INTERPRETES---------")
        for interprete in interpretes:
            print(interprete)
        
    def search_by_name(self, nome):
        sql_query = "SELECT nome FROM interprete WHERE nome = %s"
        params = (nome,)  
        result = DatabaseService().search(sql_query, params)

        if result:
            print(result[0]['nome'])
            return result[0]['nome']
        
        logger.error(f"Nenhum intérprete de nome '{nome}' encontrado")
        
    def delete_interprete(self,cod_inter):
        sql_query="delete from interprete where cod_inter = %s"
        params=(cod_inter,)
        DatabaseService().delete(sql_query,params)
        
    def update_name(self,cod_inter,novo_nome):
        sql_query = "UPDATE interprete SET nome = %s WHERE cod_inter = %s"
        params=(novo_nome,cod_inter)
        DatabaseService().update(sql_query,params)
        
    def update_type(self,cod_inter,novo_tipo):
        sql_query="UPDATE interprete SET tipo= %s where cod_inter =%s"
        params=(novo_tipo,cod_inter)
        DatabaseService().update(sql_query,params)
        
        
        

        
  
        
        

