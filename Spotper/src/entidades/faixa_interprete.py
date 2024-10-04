from src.enums.enums import MeioFisico

class Faixa_interprete():
    def __init__(self,cod_faixa,cod_alb,meio:MeioFisico,cod_inter):
        self.cod_faixa=cod_faixa
        self.cod_alb=cod_alb
        self.meio=meio
        self.cod_inter=cod_inter
        