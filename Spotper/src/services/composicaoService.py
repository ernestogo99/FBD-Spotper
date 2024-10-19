from entidades.composicao import Composicao
from database.database import DatabaseService
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class ComposicaoService:
    def __init__(self):
        pass
    
    def add_to_db(self):
        composicao=Composicao()
        sql_query="INSERT into composicao (descricao,tipo) VALUES (%s,%s) returning cod_comp"
        params=(composicao.descricao,composicao.tipo)
        result=DatabaseService().insert(sql_query,params,True)
        return result["cod_comp"]
        
    def view_all_compositions(self):
        sql_query="select * from composicao"
        composicoes=DatabaseService().search(sql_query)
        print("--------COMPOSIÇÕES-----------")
        for composicao in composicoes:
            print(composicao)
        
    
    def search_by_description(self, descricao):
        sql_query = "SELECT * FROM composicao WHERE descricao ILIKE %s"
        params = ('%' + descricao + '%',)  
        result = DatabaseService().search(sql_query, params)

        if result:
            print(result)
            return result

        logger.error(f"Nenhuma composição com descrição '{descricao}' encontrada")
    
    