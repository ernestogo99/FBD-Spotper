from entidades.faixa_playlist import Faixa_playlist

from database.database import DatabaseService

class FaixaPlaylistService:
    def __init__(self):
         pass
     
    def add_to_db(self,cod_faixa,meio,cod_alb,cod_play):
        faixa_playlist=Faixa_playlist(cod_faixa,meio,cod_alb,cod_play)
        sql_query="insert into faixa_playlist (cod_play,cod_faixa,meio,cod_alb,dt_ultima_reproducao,qtd_reproducoes) values (%s,%s,%s,%s,%s,%s)"
        params=(faixa_playlist.cod_play,faixa_playlist.cod_faixa,faixa_playlist.meio,faixa_playlist.cod_alb,faixa_playlist.dt_ultima_reproducao,faixa_playlist.qtd_reproducoes)
        DatabaseService().insert(sql_query,params)
        
    def view_faixas_with_playlist(self):
        sql_query="select faixa.cod_faixa,descricao,fp.cod_play,fp.qtd_reproducoes,fp.dt_ultima_reproducao from faixa inner join faixa_playlist fp on faixa.cod_faixa=fp.cod_faixa"
        faixas=DatabaseService().search(sql_query)
        print("--------FAIXAS E PLAYLISTS----------")
        for faixa in faixas:
            print(f"{faixa['cod_faixa']} | {faixa['descricao']} | {faixa['cod_play']} | {faixa['qtd_reproducoes']} | {faixa['dt_ultima_reproducao']}")
            
    
   
    
    def update_faixas_in_playlist(self,cod_faixa,nova_qtd_reproducoes):
        sql_query="update faixa_playlist set qtd_reproducoes =%s where cod_faixa =%s"
        params=(nova_qtd_reproducoes,cod_faixa)
        DatabaseService().update(sql_query,params)
        
   
        
    
    def delete_faixas_in_playlist(self,cod_faixa):
        sql_query="delete from faixa_playlist where cod_faixa= %s"
        params=(cod_faixa,)
        DatabaseService().delete(sql_query,params)
        


