# pylint: disable=all
from entidades.playlist import Playlist
from database.database import DatabaseService
import logging
from services.albumService import AlbumService
from services.faixaPlaylistService import FaixaPlaylistService
from utils.enumsUtils import check_meio_fisico
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
    
   
    def view_playlists():
        sql_query="select * from playlist"
        playlists=DatabaseService().search(sql_query)
        print("---------PLAYLISTS----------")
        for playlist in playlists:
            print(playlist)
      
    @staticmethod  
    def view_playlist_by_name(name):
        sql_query="select * from playlist where nome = %s"  
        params=(name,)
        result=DatabaseService().search(sql_query,params)
        
        if result:
            print(result)
            return result[0]["cod_play"]
            
        logger.error("Playlist não encontrada")
        return None
        
    @staticmethod    
    def delete_playlist(cod_play):
        sql_query="delete from playlist where cod_play = %s"
        params=(cod_play,)
        DatabaseService().delete(sql_query,params)
     
     
    def view_faixas_in_playlist_by_id(self,cod_play):
        sql_query="select fp.cod_faixa,p.cod_play,p.nome from playlist p inner join faixa_playlist fp on fp.cod_play=p.cod_play where p.cod_play=%s"
        params=(cod_play,)
        faixas=DatabaseService().search(sql_query,params)
        print("--------FAIXA E PLAYLIST----------")
        for faixa in faixas:
            print(f"cod_faixa: {faixa['cod_faixa']} | nome_playlist: {faixa['nome']} | cod_play: {faixa['cod_play']}")
        return faixas   
      
    def playlist_maintance(self,option):
        self.view_playlists()
        if option == 1:
            cod_play=int(input("Selecione o código da playlist que deseja atualizar: "))
            AlbumService().show_albums()
            descricao=str(input("Digite a descrição do album que voce deseja para visualizar suas faixas: "))
            cod_alb=AlbumService().search_by_description(descricao)
            faixas=AlbumService().show_faixas_by_album(cod_alb)
            if len(faixas)==0:
                logger.error("Este álbum não possui faixas.")
                return
            meio=check_meio_fisico("Digite o meio físico (CD, VINIL, DOWNLOAD): ")
            cod_faixa=int(input("Digite o código da faixa que deseja adicionar a playlist: "))
            FaixaPlaylistService().add_to_db(cod_faixa,meio,cod_alb,cod_play)
        else:
            cod_play=int(input("Selecione o código da playlist para visualizar suas músicas: "))
            faixas=self.view_faixas_in_playlist_by_id(cod_play)
            if len(faixas)==0:
                logger.error("Essa playlist não possui faixas")
                return 
            cod_faixa=int(input("Digite o código da faixa que deseja remover da playlist: "))
            FaixaPlaylistService().delete_faixas_in_playlist(cod_faixa)
            
    @staticmethod         
    def query_4():
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
        