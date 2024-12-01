# pylint: disable=all
from services.faixaPlaylistService import FaixaPlaylistService
from services.faixaService import FaixaService
from services.gravadoraService import GravadoraService
from services.interpreteService import InterpreteService
from services.compositorService import CompositorService
from services.playlistService import PlaylistService
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def update():
    while True:
        print("\nEscolha a opção que deseja atualizar no spotper: \n")
        print("1-Faixa playlist")
        print("2-faixa")
        print("3-Gravadora")
        print("4-Interprete")
        print("5-Compositor")
        print("6-Playlist")
        print("0-voltar")
        
        option = input("\nDigite a opção desejada: ")
        match option:
            case "1":
                update_faixa_playlist()
            
            case "2":
                update_faixa()
                
            case "3":
                update_gravadora()
                
            case "4":
                update_interprete()
                
            case "5":
                update_compositor()
            
            case "6":
                playlist_update_maintance()
                
            case "0":
                return
            
            case _:
                logger.error("Opção inválida,tente novamente")  
                
                
def update_faixa_playlist():
    FaixaPlaylistService().view_faixas_in_playlist()
    cod_faixa=int(input("Digite o código da faixa que deseja atualizar: "))
    qtd_reprod=int(input("Digite a nova quantidade de reproduções: "))
    FaixaPlaylistService().update_faixas_in_playlist(cod_faixa,qtd_reprod)
    

def update_faixa():
    FaixaService().view_all_faixas()
    cod_faixa=int(input("Digite o código da faixa que deseja atualizar: "))
    nova_desc=str(input("Digite a nova descrição da faixa: "))
    FaixaService().update_description(cod_faixa,nova_desc)
    
def update_gravadora():
    GravadoraService().view_all_grav()
    cod_grav=int(input("Digite o código da gravadora que deseja atualizar: "))
    nova_sede=str(input("Digite a nova sede da gravadora: "))
    nova_homepg=str(input("Digite a nova home page da gravadora: "))
    GravadoraService().update_homepg(cod_grav,nova_homepg)
    GravadoraService().update_sede(cod_grav,nova_sede)
    
def update_interprete():
    InterpreteService.view_all_interpretes()
    cod_inter=int(input("Digite o código do interprete que deseja atualizar: "))
    new_name=str(input("Digite o novo nome do interprete: "))
    new_type=str(input("Digite o novo tipo do interprete: "))
    InterpreteService.update_name(cod_inter,new_name)
    InterpreteService.update_type(cod_inter,new_type)
    
def update_compositor():
    CompositorService().update_death_date()
    
def playlist_update_maintance():
    option=int(input("Digite 1 para adicionar uma música na playlist e 2 para remover "))
    PlaylistService().playlist_maintance(option)