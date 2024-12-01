# pylint: disable=all
from services.compositorService import CompositorService
from services.albumService import AlbumService
from services.composicaoService import ComposicaoService
from services.faixaCompositorService import FaixaCompositorService
from services.faixaInterpreteService import FaixaInterpreteService
from services.faixaPlaylistService import FaixaPlaylistService
from services.faixaService import FaixaService
from services.gravadoraService import GravadoraService
from services.interpreteService import InterpreteService
from services.periodoMusicalService import PeriodoMusicalService
from services.playlistService import PlaylistService
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def view():
    while True:   
        print("\nSelecione o que deseja ver  no Spotper: \n")
        print("1 - Albums")
        print("2 - Faixas")
        print("3 - Composições")
        print("4 - Compositores")
        print("5 - Faixa-Compositor")
        print("6 - Faixa-Interprete")
        print("7 - Faixa-Playlist")
        print("8 - Gravadoras")
        print("9 - Intérpretes")
        print("10 - Períodos Musicais")
        print("11 - Playlists")
        print("12- faixas nos albums")
        print("13- Consultas solicitadas")
        print("14- Gravadoras e seus telefones")
        print("0 - Sair")

        option = input("\nDigite a opção desejada: ")

        match option:
            case "1":
                view_album()
            case "2":
                view_faixa()
            case "3":
                view_composicoes()
            case "4":
                view_compositores()
            case "5":
                view_faixa_compositor()
            case "6":
                view_faixa_interprete
            case "7":
                view_faixa_playlist()
            case "8":
                view_gravadoras()
            case "9":
                view_interprete()
            case "10":
                view_periodo_musical()
            case "11":
                view_playlist()
            case "12":
                view_faixas_album()
            case "13":
                view_queries()            
            case "14":
                view_phones()                              
            case "0":
                return
            case _:
                logger.error("Opção inválida,tente novamente")
                


def view_album():
    AlbumService().show_albums()
    
def view_faixas_album():
    AlbumService().show_faixas_in_album()
    
def view_faixa():
    FaixaService().view_all_faixas()
    
def view_composicoes():
    ComposicaoService().view_all_compositions()
    
def view_compositores():
    CompositorService().view_all_compositores()
    
def view_faixa_compositor():
    FaixaCompositorService().view_faixa_compositor()
    
def view_faixa_interprete():
    FaixaInterpreteService().view_faixa_interprete()
    
def view_faixa_playlist():
    FaixaPlaylistService().view_faixas_with_playlist()
    
def view_gravadoras():
    GravadoraService().view_all_grav()
    
def view_interprete():
    InterpreteService().view_all_interpretes()
    
def view_periodo_musical():
    PeriodoMusicalService().view_all_PM()
    
def view_playlist():
    PlaylistService().view_playlists()
   
def view_phones():
    GravadoraService().view_grav_phones()  
    
def view_queries():
    GravadoraService().query_2()
    CompositorService().query_3()
    PlaylistService().query_4()
    AlbumService().query_1()
    return