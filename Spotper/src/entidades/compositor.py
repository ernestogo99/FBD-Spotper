from utils.timeUtils import input_data

class Compositor:
    def __init__(self):
        self.nome=str(input("Digite o nome do compositor: "))
        self.dt_nascimento=input_data("Digite a data de nascimento do compositor (ANO-MES-DIA): ")
        self.cidade=str(input("Digite a cidade onde o compositor nasceu: "))
        self.pais=str(input("Digite o pais onde o compositor nasceu: "))
        self.local_nascimento=(self.cidade,self.pais)
        
        dead=str(input("O compositor já morreu? (sim/nao) ").lower())
        if dead=="sim":
            self.dt_morte=input_data("Digite a data da morte do compositor(ANO-MES-DIA) :")
        else:
            self.dt_morte=None
        
        
        
