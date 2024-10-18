# pylint: disable=all
from entidades.gravadora import Gravadora
from  database.database import DatabaseService
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class GravadoraService:
    def __init__(self):
        pass

    def add_to_db(self):
        gravadora = Gravadora()
        
       
        sql_query = "INSERT INTO gravadora (nome, sede, home_pg) VALUES (%s, %s, %s) RETURNING cod_grav"
        params = (gravadora.nome, gravadora.sede, gravadora.home_pg)
        
        result = DatabaseService().insert(sql_query, params,True)
        
        if result:
            cod_grav = result["cod_grav"]
            
           
            for phone in gravadora.phones:
                sql_query = "INSERT INTO telefone_gravadora (cod_grav, numero) VALUES (%s, %s)"
                params = (cod_grav, phone)
                DatabaseService().insert(sql_query, params)
            
            logger.info(f"Gravadora '{gravadora.nome}' e seus telefones foram inseridos com sucesso.")
            return cod_grav
       
        logger.error("Erro ao inserir a gravadora.")
        return None
    
    def view_all_grav(self):
        sql_query="select * from gravadora"
        gravadoras=DatabaseService().search(sql_query)
        print("---------GRAVADORAS-----------")
        for gravadora in gravadoras:
            print(gravadora)
            
    def search_by_name(self,name):
        sql_query="select * from gravadora where nome =%s"
        params=(name,)
        result=DatabaseService().search(sql_query,params)
        if result:
            print(result)
            return result[0]["cod_grav"]
        logger.error(f"nenhuma gravadora com nome {name} encontrada")
        
        
    def delete_grav_by_name(self,name):
        sql_query="delete from gravadora where nome= %s"
        params=(name,)
        DatabaseService().delete(sql_query,params)
        
    def update_sede_grav_by_name(self,sede,name):
        sql_query="update gravadora set sede = %s where nome =%s"
        params=(sede,name)
        DatabaseService().update(sql_query,params)
        
    def update_homepg_grav(self,home_pg,name):
        sql_query="update gravadora set home_pg =%s where nome =%s"
        params=(home_pg,name)
        DatabaseService().update(sql_query,params)
        
    