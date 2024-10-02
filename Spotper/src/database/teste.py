# pylint: disable=all
from venv import logger
from database import DatabaseService




class Interprete:
    def __init__(self):
        self.nome=str(input("Digite o nome do interprete: "))
        self.tipo=str(input("Digite o tipo de interpretação: "))

class InterpreteService:
    def __init__(self):
        pass
    
    def add_to_db(self):
        interprete=Interprete()
        sql_query="INSERT INTO interprete(nome,tipo)  VALUES (%s,%s)"
        params=(interprete.nome,interprete.tipo)
        DatabaseService().insert(sql_query,params)
        return interprete.nome

    def view_all_interpretes(self):
        sql_query="SELECT nome,tipo FROM interprete"
        interpretes=DatabaseService().search(sql_query)
        print("--------INTERPRETES---------")
        for interprete in interpretes:
            print(interprete["nome"], interprete["tipo"])
            
    def search_by_name(self, nome):
        sql_query = "SELECT * FROM interprete WHERE nome = %s"
        params = (nome,)  
        result = DatabaseService().search(sql_query, params)

        if result:
            print(result[0])
            return result[0]["nome"]  
        
        logger.error(f"Nenhum intérprete de nome '{nome}' encontrado")
        
    def delete_by_name(self,nome):
        sql_query="delete from interprete where nome = %s"
        params=(nome,)
        DatabaseService().delete(sql_query,params)
        

        
        


def main():
    db_service = DatabaseService()
   

    interprete_service = InterpreteService()
    
   
   
    
    interprete_service.view_all_interpretes()
    interprete_service.search_by_name("ernestogo")
    db_service.close_connection()
if __name__ == "__main__":
    main()