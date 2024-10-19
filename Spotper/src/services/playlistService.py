from entidades.playlist import Playlist
from database.database import DatabaseService
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class PlaylistService:
    def __init__(self):
        pass
    
    def add_to_db(self):
        playlist=Playlist()
        sql_query="insert into playlist (nome,dt_criacao,t_exec) values (%s,%s,%s) returning cod_play "
        params=(playlist.nome,playlist.dt_criacao,playlist.t_exec)
        result=DatabaseService().insert(sql_query,params,True)
        
        if result:
            cod_play=result["cod_play"]
            return cod_play
        
        logger.error("Erro ao inserir playlist")
        return None
        
    def view_playlists(self):
        sql_query="select * from playlist"
        playlists=DatabaseService().search(sql_query)
        print("---------PLAYLISTS----------")
        for playlist in playlists:
            print(playlist)
      
      
    def view_playlist_by_name(self,name):
        sql_query="select * from playlist where nome = %s"  
        params=(name,)
        result=DatabaseService().search(sql_query,params)
        
        if result:
            print(result)
            return result[0]["cod_play"]
            
        logger.error("Playlist não encontrada")
        return None
        
        
    def delete_playlist(self,cod_play):
        sql_query="delete from playlist where cod_play = %s"
        params=(cod_play,)
        DatabaseService().delete(sql_query,params)
           
        
    def query_4(self):
        sql_query="""
            SELECT p.nome AS playlist_nome
            FROM playlist p
            JOIN faixa_playlist fp ON p.cod_play = fp.cod_play
            JOIN faixa f ON fp.cod_faixa = f.cod_faixa AND fp.cod_alb = f.cod_alb AND fp.meio = f.meio
            JOIN composicao c ON f.cod_comp = c.cod_comp
            JOIN compositor comp ON f.cod_comp = comp.cod_comp
            JOIN periodo_musical pm ON comp.cod_pm = pm.cod_pm
            WHERE c.tipo = 'Concerto' 
            AND pm.descricao = 'barroco'
            GROUP BY p.nome,p.cod_play
            HAVING COUNT(f.cod_faixa) = (
            SELECT COUNT(fp2.cod_faixa)
            FROM faixa_playlist fp2
            WHERE fp2.cod_play = p.cod_play
            );
        """
        print("Playlists cujas faixas tem tipo de composição concerto e barroco")
        playlists=DatabaseService().search(sql_query)
        for playlist in playlists:
            print(f"{playlist['playlist_nome']}")
        