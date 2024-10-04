from datetime import datetime
from src.enums.enums import MeioFisico

class Faixa_playlist:
    def __init__(self,cod_play,cod_faixa,meio:MeioFisico,cod_alb):
        dt_ultima_reproducao=str(input("Digite a data da ultima reprodução(ano-mes-dia): "))
        self.dt_ultima_reproducao=datetime.strptime(dt_ultima_reproducao,"%Y-%m-%d")
        self.qtd_reproducoes=int(input("Digite a quantidade de reproduções: "))
        self.cod_play=cod_play
        self.cod_faixa=cod_faixa
        self.meio=meio
        self.cod_alb=cod_alb