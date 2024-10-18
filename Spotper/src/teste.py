from database.database import DatabaseService
from services.faixaService import FaixaService


def main():
    db_service = DatabaseService()
   

    
    faixaservice=FaixaService()
   
    faixaservice.add_to_db()
    
    
  

    
    
   
    db_service.close_connection()
if __name__ == "__main__":
    main()