from utils.timeUtils import input_data

class Faixa_playlist:
    def __init__(self,cod_faixa,meio,cod_alb,cod_play):
        self.dt_ultima_reproducao=input_data("Digite a data da ultima reprodução(ano-mes-dia): ")
        self.qtd_reproducoes=int(input("Digite a quantidade de reproduções: "))
        self.cod_faixa=cod_faixa
        self.meio=meio
        self.cod_alb=cod_alb
        self.cod_play=cod_play