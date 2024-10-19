
from datetime import datetime
from enums.enums import Gravacao,MeioFisico



class Faixa:
    def __init__(self):
        self.descricao=str(input("Digite a descrição da faixa: "))
        self.num_faixa=int(input("Digite o número da faixa: "))
        tempo=str(input("digite o tempo de execução da faixa (hora:min:seg): "))
        self.t_execucao=datetime.strptime(tempo,"%H:%M:%S").time()
        self.tipo_grav=Gravacao[input("Digite o tipo de gravação(ADD OU DDD): ").upper()].value
        self.meio=MeioFisico[input("Digite o meio físico (CD, VINIL, DOWNLOAD): ").upper()].value
      
        