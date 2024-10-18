# pylint: disable=all
from entidades.compositor import Compositor
from entidades.periodo_musical import PeriodoMusical
from services.periodoMusicalService import PeriodoMusicalService
from database.database import DatabaseService
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class CompositorService:
    def __init__(self):
        pass
    
    def add_to_db(self, novo_periodo=False):
        compositor = Compositor()
        
        if novo_periodo:
            result=PeriodoMusicalService().add_to_db()
            cod_periodo = result["cod_pm"]
            
            
        else:
            PeriodoMusicalService().view_all_PM()
            cod_periodo = int(input("Veja o código do período musical que você deseja relacionar o compositor e coloque aqui: "))
        
        if compositor.dt_morte is not None:
            sql_query = "INSERT INTO compositor (nome, dt_nasc, dt_morte, local_nascimento, cod_pm) VALUES (%s, %s, %s, %s, %s) returning cod_comp"
            params = (compositor.nome, compositor.dt_nascimento, compositor.dt_morte, compositor.local_nascimento, cod_periodo)
        else:
            sql_query = "INSERT INTO compositor (nome, dt_nasc, local_nascimento, cod_pm) VALUES (%s, %s, %s, %s) returning cod_comp"
            params = (compositor.nome, compositor.dt_nascimento, compositor.local_nascimento, cod_periodo)
        
        result=DatabaseService().insert(sql_query, params,True)
        
        if result:
            return result
        
        else:
            logger.error("Erro ao inserir o compositor")
            return None
    
    def view_all_compositores(self):
        sql_query = "SELECT * FROM compositor"
        compositores = DatabaseService().search(sql_query)
        print("-------COMPOSITORES----------")
        for compositor in compositores:
            print(compositor)
    
    def search_by_name(self, name):
        sql_query = "SELECT * FROM compositor WHERE nome = %s"
        params = (name,)
        result = DatabaseService().search(sql_query, params)
        
        if result:
            print(result)
            return result
        
        logger.error(f"Nenhum compositor com nome: '{name}' encontrado")
    
    def update_death_date(self):
        self.view_all_compositores()
        nome_compositor = str(input("Digite o nome do compositor que deseja atualizar: "))
        new_death_date = str(input("Digite a data de morte do compositor (YYYY-MM-DD): "))
        
        death_date = datetime.strptime(new_death_date, "%Y-%m-%d")
        
        sql_query = "UPDATE compositor SET dt_morte = %s WHERE nome = %s"
        params = (death_date, nome_compositor)
        DatabaseService().update(sql_query, params)
