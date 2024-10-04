from datetime import datetime


class Compositor:
    def __init__(self):
        self.nome=str(input("Digite o nome do compositor: "))
        self.dt_nascimento=self.input_data("Digite a data de nascimento do compositor (ANO-MES-DIA):")
        self.cidade=str(input("Digite a cidade onde o compositor nasceu: "))
        self.pais=str(input("Digite o pais onde o compositor nasceu"))
        self.local_nascimento=(self.cidade,self.pais)
        
        self.cod_pm=int(input("Digite o código do periodo musical a qual este compositor se relaciona"))
        
        dead=str(input("O compositor já morreu? (sim/nao)").lower())
        if dead=="sim":
            self.dt_morte=self.input_data("Digite a data da morte do compositor(ANO-MES-DIA) :")
        else:
            self.dt_morte=None
        
        
        
    def input_data(self, prompt):
        while True:
            try:
                data_str = input(prompt)
                return datetime.strptime(data_str, "%Y-%m-%d")
            except ValueError:
                print("Formato de data inválido. Tente novamente.")