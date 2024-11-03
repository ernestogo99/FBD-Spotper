# pylint: disable=all
from utils.timeUtils import input_data
from utils.enumsUtils import check_periodo


class PeriodoMusical:
    def __init__(self):
        self.descricao = check_periodo("Digite a descrição do período musical: ")
        self.inicio = input_data("Digite a data inicial do intervalo (YYYY-MM-DD): ")
        self.fim = input_data("Digite a data final do intervalo (YYYY-MM-DD): ")
        self.interv_tempo =self.formatar_interv_tempo(self.inicio,self.fim)
         
  
                   
    def formatar_interv_tempo(self, inicio, fim):
        return f"[{inicio},{fim}]"
