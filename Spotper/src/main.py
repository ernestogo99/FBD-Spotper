from database.database import DatabaseService
from actions.add import add
from actions.update import update
from actions.delete import delete
from actions.view import view

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    db_service = DatabaseService()
    while True:
        print("\n Escolha umas opções abaixo: \n")
        print("1-adicionar")
        print("2-editar")
        print("3-visualizar")
        print("4-excluir")
        print("5-sair")
        
        option=int(input("\n"))
        
        match option:
            case 1:
                add()
            case 2:
                update()
            case 3:
                view()
            case 4:
                delete()
            case 5:
                db_service.close_connection()
                exit()
            case _:
                logger.error("Opcao invalida. Tente novamente")
                
                
if __name__ == "__main__":
    main()