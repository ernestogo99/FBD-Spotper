from utils.timeUtils import input_data
from utils.enumsUtils import check_meio_fisico

class Faixa_playlist:
    def __init__(self):
        self.dt_ultima_reproducao=input_data("Digite a data da ultima reprodução(ano-mes-dia): ")
        self.qtd_reproducoes=int(input("Digite a quantidade de reproduções: "))
        self.cod_faixa=int(input("Digite o código da faixa que deseja relacionar a playlist: "))
        self.meio=check_meio_fisico("Digite o meio físico (CD, VINIL, DOWNLOAD): ")
        self.cod_alb=int(input("Digite o código do album que deseja relacionar: "))
        self.cod_play=int(input("Digite o código da playlist  que deseja relacionar: "))