# pylint: disable=all
from services.faixaPlaylistService import FaixaPlaylistService
from services.faixaService import FaixaService
from services.gravadoraService import GravadoraService
from services.interpreteService import InterpreteService
from services.playlistService import PlaylistService
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def delete():
    while True:
        print("\nEscolha a opção que deseja deletar do spotper: \n")
        print("1-Faixa playlist")
        print("2-faixa")
        print("3-Gravadora")
        print("4-Interprete")
        print("5-playlist")
        print("0-voltar")
        
        option = input("\nDigite a opção desejada: ")
        match option:
            case "1":
                del_faixa_playlist()
            
            case "2":
                del_faixa()
                
            case "3":
                del_gravadora()
                
            case "4":
                del_interprete()
                
            case "5":
                del_playlist()
                
            case "0":
                return
            
            case _:
                logger.error("Opção inválida,tente novamente")                          

def del_faixa_playlist():
    FaixaPlaylistService().view_faixas_in_playlist()
    cod_faixa=int(input("Digite o código da faixa que deseja excluir: "))
    FaixaPlaylistService().delete_faixas_in_playlist(cod_faixa)
    
def del_faixa():
    FaixaService().view_all_faixas()
    cod_faixa=int(input("Digite o código da faixa que deseja excluir: "))
    FaixaService().delete_by_cod(cod_faixa)
    
def del_gravadora():
    GravadoraService().view_all_grav()
    cod_grav=int(input("Digite o código da gravadora que deseja excluir: "))
    GravadoraService().delete_grav(cod_grav)
    
    
def del_interprete():
    InterpreteService().view_all_interpretes()
    cod_interprete=int(input("Digite o código do interprete que deseja excluir: "))
    InterpreteService().delete_interprete(cod_interprete)
    
def del_playlist():
    PlaylistService().view_playlists()
    cod_play=int(input("Digite o código da playlist que deseja excluir"))
    PlaylistService().delete_playlist(cod_play)