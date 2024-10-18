# pylint: disable=all
from datetime import datetime
from enums.enums import Periodo

    


class PeriodoMusical:
    def __init__(self):
      
        descricao_input = input("Digite a descrição do período musical: ").lower()

     
        periodo_encontrado = None
        for periodo in Periodo:
            if periodo.value.lower() == descricao_input:
                periodo_encontrado = periodo.value
                break

        if periodo_encontrado is None:
            print(f"Período '{descricao_input}' inválido. Por favor, insira um valor válido do enum Periodo.")
            return
        
        self.descricao = periodo_encontrado 
        self.inicio = self.input_data("Digite a data inicial do intervalo (YYYY-MM-DD): ")
        self.fim = self.input_data("Digite a data final do intervalo (YYYY-MM-DD): ")
        self.interv_tempo =self.formatar_interv_tempo(self.inicio,self.fim)
         
    def input_data(self, prompt):
        while True:
            try:
                data_str = input(prompt)
                return datetime.strptime(data_str, "%Y-%m-%d").date()
            except ValueError:
                print("Formato de data inválido. Tente novamente.")
                
                   
    def formatar_interv_tempo(self, inicio, fim):
        return f"[{inicio},{fim}]"
