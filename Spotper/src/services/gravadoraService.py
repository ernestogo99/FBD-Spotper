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
            
            params=[]
            for phone in gravadora.phones:
                params.append((cod_grav, phone))
               
            sql_query = "INSERT INTO telefone_gravadora (cod_grav, numero) VALUES (%s, %s)"
            DatabaseService().insert_many(sql_query, params)
            logger.info(f"Gravadora '{gravadora.nome}' e seus telefones foram inseridos com sucesso.")
            return cod_grav
       
        logger.error("Erro ao inserir a gravadora.")
        return None
    
    @staticmethod
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
        
        
    def delete_grav(self,cod_grav):
        sql_query="delete from gravadora where cod_grav= %s"
        params=(cod_grav,)
        DatabaseService().delete(sql_query,params)
        
    def update_sede(self,sede,cod_grav):
        sql_query="update gravadora set sede = %s where cod_grav =%s"
        params=(sede,cod_grav)
        DatabaseService().update(sql_query,params)
        
    def update_homepg(self,home_pg,cod_grav):
        sql_query="update gravadora set home_pg =%s where cod_grav =%s"
        params=(home_pg,cod_grav)
        DatabaseService().update(sql_query,params)
        
    def query_2(self):
        sql_query="""
                SELECT g.nome, COUNT(DISTINCT p.cod_play) AS total_playlists
                FROM gravadora g
                JOIN album a ON g.cod_grav = a.cod_grav
                JOIN faixa f ON a.cod_alb = f.cod_alb AND a.meio = f.meio
                JOIN faixa_compositor fc ON f.cod_faixa = fc.cod_faixa AND f.cod_alb = fc.cod_alb AND f.meio = fc.meio
                JOIN compositor c ON fc.cod_comp = c.cod_comp
                JOIN faixa_playlist fp ON f.cod_faixa = fp.cod_faixa AND f.cod_alb = fp.cod_alb AND f.meio = fp.meio
                JOIN playlist p ON fp.cod_play = p.cod_play
                WHERE c.nome = 'Dvorack'
                GROUP BY g.nome
                ORDER BY total_playlists DESC
                LIMIT 1;
        """
        print("--------Gravadora com maior número de playlist ---------")
        gravadoras=DatabaseService().search(sql_query)
        for gravadora in gravadoras:
            print(f"{gravadora['nome']} | {gravadora['total_playlists']}")
            