from datetime import datetime
from enums.enums import MeioFisico

class Faixa_playlist:
    def __init__(self):
        dt_ultima_reproducao=str(input("Digite a data da ultima reprodução(ano-mes-dia): "))
        self.dt_ultima_reproducao=datetime.strptime(dt_ultima_reproducao,"%Y-%m-%d")
        self.qtd_reproducoes=int(input("Digite a quantidade de reproduções: "))
        self.cod_faixa=int(input("Digite o código da faixa que deseja relacionar a playlist: "))
        self.meio=MeioFisico[input("Digite o meio físico (CD, VINIL, DOWNLOAD): ").upper()].value
        self.cod_alb=int(input("Digite o código do album que deseja relacionar: "))
        self.cod_play=int(input("Digite o código da playlist  que deseja relacionar: "))