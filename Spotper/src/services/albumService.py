# pylint: disable=all
from entidades.album import Album
from services.gravadoraService import GravadoraService
from database.database import DatabaseService
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class AlbumService:
    def __init__(self):
        pass
    
    
    def add_to_db(self,new_grav=False):
        album=Album()
        
        if new_grav:
           cod_grav=GravadoraService().add_to_db()
        
        else:
            GravadoraService().view_all_grav()
            cod_grav=int(input("Digite o código da gravadora que deseja adicionar: "))
           
        
        sql_query="insert into album (nome,meio,cod_grav,descricao,data_grav,pr_compra,tipo_compra) values (%s,%s,%s,%s,%s,%s,%s) returning cod_alb"
        params=(album.nome,album.meio,cod_grav,album.descricao,album.data_grav,album.pr_compra,album.tipo_compra)  
        
        result=DatabaseService().insert(sql_query,params,True)
        
        if result:
            return result["cod_alb"]
        
       
        logger.error("Erro ao inserir o album")
        return None
        
        
    def show_albums(self):
        sql_query="select * from album"
        albums=DatabaseService().search(sql_query)
        print("---------ALBUMS----------")
        for album in albums:
            print(album)
            
            
    def search_by_description(self, descricao):
        sql_query = "SELECT * FROM album WHERE descricao ILIKE %s"
        params = ('%' + descricao + '%',)  
        result = DatabaseService().search(sql_query, params)

        if result:
            print(result)
            return result[0]["cod_alb"]

        logger.error(f"Nenhum album com descrição '{descricao}' encontrado") 
        
    
    def show_faixas_in_album(self):
        sql_query="""
            select a.cod_alb,a.nome,f.descricao,f.cod_faixa from faixa f inner join
            album a on a.cod_alb=f.cod_alb
        """ 
        faixas_album=DatabaseService().search(sql_query)
        print("-----ALBUMS E FAIXAS------")
        for faixa in faixas_album:
             print(f"{faixa['cod_alb']} | {faixa['nome']} | {faixa['descricao']} | {faixa['cod_faixa']} ") 
        
    def show_faixas_by_album(self,cod_alb):
        sql_query="""
            select a.cod_alb,a.nome,f.descricao,f.cod_faixa from faixa f inner join
            album a on a.cod_alb=f.cod_alb where a.cod_alb=%s
        """ 
        params=(cod_alb,)
        faixas_album=DatabaseService().search(sql_query,params)
        print("-----ALBUMS E FAIXAS------")
        for faixa in faixas_album:
             print(f"{faixa['cod_alb']} | {faixa['nome']} | {faixa['descricao']} | {faixa['cod_faixa']} ") 
        return faixas_album
        
        
    def query_1(self):
        sql_query="""
           SELECT nome, pr_compra
            FROM album
            WHERE pr_compra > (SELECT AVG(pr_compra) FROM album);
        """
        albums=DatabaseService().search(sql_query)
        print("-------ALBUMS E PREÇOS MAIORES QUE A MÉDIA--------")
        for album in albums:
            print(f"{album['nome']} | {album['pr_compra']}")
        