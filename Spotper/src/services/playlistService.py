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
        
        
    def delete_playlist_by_name(self,name):
        sql_query="delete from playlist where nome = %s"
        params=(name,)
        DatabaseService().delete(sql_query,params)
           
        
       