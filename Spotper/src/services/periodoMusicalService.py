# pylint: disable=all
from entidades.periodo_musical import PeriodoMusical
from database.database import DatabaseService
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class PeriodoMusicalService:
    def __init__(self):
        pass
    
    def add_to_db(self):
        periodo_musical = PeriodoMusical()
        sql_query = "INSERT INTO periodo_musical (descricao, interv_tempo) VALUES (%s, %s) RETURNING cod_pm"
        params = (periodo_musical.descricao, periodo_musical.interv_tempo)

        result = DatabaseService().insert(sql_query, params,True)  

        if result:
            return result
        else:
            logger.error("Erro ao inserir período musical")
            return None
    
    @staticmethod    
    def view_all_PM():
        sql_query="select * from periodo_musical"
        periodos=DatabaseService().search(sql_query)
        print("--------PERIODOS MUSICAIS---------")
        for periodo in periodos:
            print(periodo)
            
    @staticmethod  
    def search_by_description(descricao):
        sql_query = "SELECT * FROM periodo_musical WHERE descricao::TEXT ILIKE %s"
        params = ('%' + descricao + '%',)  
        result = DatabaseService().search(sql_query, params)

        if result:
            print(result)
            return result

        logger.error(f"Nenhuma composição com descrição '{descricao}' encontrada")
     
        