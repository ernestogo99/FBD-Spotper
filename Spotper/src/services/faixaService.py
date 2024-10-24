# pylint: disable=all
import logging
from database.database import DatabaseService
from entidades.faixa import Faixa
from services.albumService import AlbumService
from services.composicaoService import ComposicaoService

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class FaixaService:
    def __init__(self):
        pass

    def add_to_db(self):
        
        faixa = Faixa()
        new_album = input("Você gostaria de adicionar um novo álbum? (sim/não): ").strip().lower()
        
        if new_album == 'sim':
            album_service = AlbumService()
            new_grav=str(input("Você gostaria de adicionar uma nova gravadora no álbum? (sim/não): ").strip().lower())
            if new_grav=='sim':
                album_id = album_service.add_to_db(new_grav=True) 
            else:
                album_id = album_service.add_to_db() 
            
        else:
            album_service = AlbumService()
            album_service.show_albums()
            album_id = int(input("Digite o código do álbum que deseja adicionar a faixa: "))

        
        new_composicao = input("Você gostaria de adicionar uma nova composição? (sim/não): ").strip().lower()
        
        if new_composicao == 'sim':
            composicao_service = ComposicaoService()
            composicao_id = composicao_service.add_to_db()
        else:
            composicao_service = ComposicaoService()
            composicao_service.view_all_compositions()
            composicao_id = int(input("Digite o código da composição que deseja associar: "))

     
        
        sql_query = "INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, meio, cod_alb, cod_comp) VALUES (%s, %s, %s, %s, %s, %s, %s) returning cod_faixa"
        params = (faixa.descricao, faixa.num_faixa, faixa.t_execucao, faixa.tipo_grav, faixa.meio, album_id, composicao_id)
        
        result = DatabaseService().insert(sql_query, params, True)
        
        if result:
            return result["cod_faixa"]
        
        logger.error("Erro ao inserir a faixa")
        return None

    def view_all_faixas(self):
        sql_query = "SELECT * FROM faixa"
        faixas = DatabaseService().search(sql_query)
        print("---------FAIXAS----------")
        for faixa in faixas:
            print(faixa)

    def search_by_description(self, descricao):
        sql_query = "SELECT * FROM faixa WHERE descricao ILIKE %s"
        params = ('%' + descricao + '%',)  
        result = DatabaseService().search(sql_query, params)

        if result:
            print(result)
            return result[0]["cod_alb"]

        logger.error(f"Nenhuma faixa com descrição '{descricao}' encontrada") 
        
    def update_description(self, cod_faixa, nova_descricao):
        sql_query = "UPDATE faixa SET descricao = %s WHERE cod_faixa = %s"
        params = (nova_descricao, cod_faixa)
        DatabaseService().update(sql_query, params)

    def delete_by_cod(self, cod_faixa):
        sql_query = "DELETE FROM faixa WHERE cod_faixa = %s"
        params = (cod_faixa,)
        DatabaseService().delete(sql_query, params)
