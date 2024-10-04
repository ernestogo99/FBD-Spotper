from src.enums.enums import MeioFisico

class Faixa_compositor:
    def __init__(self,cod_faixa,meio:MeioFisico,cod_alb,cod_compositor):
        self.cod_faixa=cod_faixa
        self.meio=meio
        self.cod_alb=cod_alb
        self.cod_compositor=cod_compositor
        