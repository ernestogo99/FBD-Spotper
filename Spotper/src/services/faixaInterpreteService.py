from entidades.faixa_interprete import Faixa_interprete

from database.database import DatabaseService

class FaixaInterpreteService:
    def __init__(self):
        pass
    
    def add_to_db(self):
        faixa_interprete=Faixa_interprete()
        sql_query="insert into faixa_interprete (cod_faixa,cod_alb,meio,cod_inter) values(%s,%s,%s,%s)"
        params=(faixa_interprete.cod_faixa,faixa_interprete.cod_alb,faixa_interprete.meio,faixa_interprete.cod_inter)
        DatabaseService().insert(sql_query,params)
        
    def view_faixa_interprete(self):
        sql_query="""
            select i.nome,f.cod_faixa from faixa_interprete f
            inner join interprete i on i.cod_inter=f.cod_inter
        """
        faixas=DatabaseService().search(sql_query)
        print("----FAIXAS E INTERPRETES----")
        for interprete in faixas:
             print(f"{interprete['cod_faixa']} | {interprete['nome']} ")