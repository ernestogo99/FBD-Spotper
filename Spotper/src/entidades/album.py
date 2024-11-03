
from utils.timeUtils import input_data
from utils.enumsUtils import check_meio_fisico


    
class Album:
    def __init__(self):
        self.nome=str(input("Digite o nome do album: "))
        self.meio=check_meio_fisico("Digite o meio físico (CD, VINIL, DOWNLOAD): ")
        self.descricao=str(input("Digite a descrição do album: ")) 
        self.data_grav=input_data("Digite a data de gravação (ano-mes-dia) : ")
        self.pr_compra=float(input("Digite o preço de compra do album: "))
        self.tipo_compra=check_meio_fisico("Digite o meio físico (CD, VINIL, DOWNLOAD): ")
      
            