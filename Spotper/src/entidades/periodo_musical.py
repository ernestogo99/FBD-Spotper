
from datetime import datetime
from src.enums.enums import Periodo

    
class PeriodoMusical:
    def __init__(self):
        self.descricao = Periodo[(input("Digite a descrição do período musical: "))]
        self.inicio = self.input_data("Digite a data inicial do intervalo (YYYY-MM-DD): ")
        self.fim = self.input_data("Digite a data final do intervalo (YYYY-MM-DD): ")
        self.interv_tempo = (self.inicio, self.fim)
         
    def input_data(self, prompt):
        while True:
            try:
                data_str = input(prompt)
                return datetime.strptime(data_str, "%Y-%m-%d")
            except ValueError:
                print("Formato de data inválido. Tente novamente.")