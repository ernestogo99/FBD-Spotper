from services.compositorService import CompositorService
from services.albumService import AlbumService
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def add():
    while True:
        print("Selecione o que deseja adicionar ao Sportper: \n")
        print("1-album\n")
        print("2-faixa\n")
        print("3-composição\n")
        print("4-compositor\n")
        
        
        

def add_album():
    opt=str(input("Deseja adicionar uma nova gravadora?(sim/não)").lower())
    if opt == "sim":
        AlbumService().add_to_db(True)
    else:
        AlbumService().add_to_db()
        