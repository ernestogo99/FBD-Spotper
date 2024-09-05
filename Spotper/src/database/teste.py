# pylint: disable=all
from database import DatabaseService


import uuid

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
        


def main():
    db_service = DatabaseService()
    print("Teste de inserção de intérprete no banco de dados")

    interprete_service = InterpreteService()
    
    # Chama o método para adicionar o intérprete ao banco
    interprete_id = interprete_service.add_to_db()
    
    # Exibe o ID do intérprete inserido
    print(f"Interprete inserido com sucesso! ID: {interprete_id}")
    db_service.close_connection()
if __name__ == "__main__":
    main()