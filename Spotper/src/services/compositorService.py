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
            PeriodoMusicalService.view_all_PM()
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

        
    def query_3(self):
        sql_query="""
                SELECT c.nome AS compositor_nome, COUNT(fp.cod_faixa) AS total_faixas
                FROM compositor c
                JOIN faixa_compositor fc ON c.cod_comp = fc.cod_comp
                JOIN faixa f ON fc.cod_faixa = f.cod_faixa AND fc.cod_alb = f.cod_alb AND fc.meio = f.meio
                JOIN faixa_playlist fp ON f.cod_faixa = fp.cod_faixa AND f.cod_alb = fp.cod_alb AND f.meio = fp.meio
                GROUP BY c.nome
                ORDER BY total_faixas DESC
                LIMIT 1;
            """
        print("-----Compositor  com maior número de faixas na playlist------")
        compositores=DatabaseService().search(sql_query)
        for compositor in compositores:
            print(f"{compositor['compositor_nome']} | {compositor['total_faixas']}")   
        