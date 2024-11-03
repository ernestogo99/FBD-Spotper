

from utils.enumsUtils import check_meio_fisico,check_gravacao
from utils.timeUtils import input_time


class Faixa:
    def __init__(self):
        self.descricao=str(input("Digite a descrição da faixa: "))
        self.num_faixa=int(input("Digite o número da faixa: "))
        self.t_execucao=input_time("digite o tempo de execução da faixa (hora:min:seg): ")
        self.tipo_grav=check_gravacao("Digite o tipo de gravação(ADD OU DDD): ")
        self.meio=check_meio_fisico("Digite o meio físico (CD, VINIL, DOWNLOAD): ")
      
        