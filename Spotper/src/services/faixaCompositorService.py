from entidades.faixa_compositor import Faixa_compositor

from database.database import DatabaseService


class FaixaCompositorService:
    def __init__(self):
        pass
    
    def add_to_db(self):
        faixa_compositor=Faixa_compositor()
        sql_query="insert into faixa_compositor (cod_faixa,meio,cod_alb,cod_comp) values (%s,%s,%s,%s)"
        params=(faixa_compositor.cod_faixa,faixa_compositor.meio,faixa_compositor.cod_alb,faixa_compositor.cod_compositor)
        DatabaseService().insert(sql_query,params)
        
        
    def view_faixa_compositor(self):
        sql_query="""
            select c.nome,fc.cod_faixa from compositor c
            inner join faixa_compositor fc  on c.cod_comp=fc.cod_comp
        """
        faixas_compositores=DatabaseService().search(sql_query)
        print("----FAIXA---COMPOSITOR----")
        for faixa in faixas_compositores:
            print(f"{faixa['cod_faixa']} | {faixa['nome']} ")
        