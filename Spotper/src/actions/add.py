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

def add():
    while True:
        print("\nSelecione o que deseja adicionar ao Spotper: \n")
        print("1 - Album")
        print("2 - Faixa")
        print("3 - Composição")
        print("4 - Compositor")
        print("5 - Faixa Compositor")
        print("6 - Faixa Interprete")
        print("7 - Faixa Playlist")
        print("8 - Gravadora")
        print("9 - Intérprete")
        print("10 - Período Musical")
        print("11 - Playlist")
        print("0 - Sair")

        option = input("\nDigite a opção desejada: ")

        match option:
            case "1":
                add_album()
            case "2":
                add_faixa()
            case "3":
                add_composicao()
            case "4":
                add_compositor()
            case "5":
                add_faixa_compositor()
            case "6":
                add_faixa_interprete()
            case "7":
                add_faixa_playlist()
            case "8":
                add_gravadora()
            case "9":
                add_interprete()
            case "10":
                add_periodo_musical()
            case "11":
                add_playlist()
            case "0":
                return
            case _:
                logger.error("Opção inválida,tente novamente")

def add_album():
    opt=str(input("Deseja adicionar uma nova gravadora?(sim/não) ").lower())
    if opt == "sim":
        AlbumService().add_to_db(True)
    else:
        AlbumService().add_to_db()


def add_compositor():
    opt=str(input("Deseja adicionar um novo periodo musical?(sim/não) ").lower())
    if opt=="sim":
        CompositorService().add_to_db(True)
        
    else:
        CompositorService().add_to_db()
        
        
def add_composicao():
    ComposicaoService().add_to_db()
    
def add_faixa_compositor():
    FaixaCompositorService().add_to_db()
    
def add_faixa_interprete():
    FaixaInterpreteService().add_to_db()
    
def add_faixa_playlist():
    FaixaPlaylistService().add_to_db()
    
def add_faixa():
    FaixaService().add_to_db()
    
def add_gravadora():
    GravadoraService().add_to_db()
    
def add_interprete():
    InterpreteService().add_to_db()
    
def add_periodo_musical():
    PeriodoMusicalService().add_to_db()
    
def add_playlist():
    PlaylistService().add_to_db()