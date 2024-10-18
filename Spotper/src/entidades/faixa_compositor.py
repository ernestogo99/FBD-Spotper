from enums.enums import MeioFisico

class Faixa_compositor:
    def __init__(self):
        self.cod_faixa=int(input("Digite o código da faixa que deseja relacionar o compositor: "))
        self.meio=MeioFisico[input("Digite o meio físico (CD, VINIL, DOWNLOAD): ").upper()].value
        self.cod_alb=int(input("Digite o código do album que deseja relacionar: "))
        self.cod_compositor=int(input("Digite o código do compositor que deseja relacionar: "))
        