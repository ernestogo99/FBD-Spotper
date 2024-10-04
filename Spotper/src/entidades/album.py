from datetime import datetime
from src.enums.enums import MeioFisico



    
class Album:
    def __init__(self):
        self.nome=str(input("Digite o nome do album: "))
        self.meio=MeioFisico[input("Digite o meio físico (CD, VINIL, DOWNLOAD): ").upper()] 
        self.cod_grav=int(input("Digite o código da gravadora que você deseja relacionar ao album"))
        self.descricao=str(input("Digite a descrição do album: ")) 
        
        data_grav=str(input("Digite a data de gravação (ano-mes-dia) : "))
        self.data_grav=datetime.strptime(data_grav,"%Y-%m-%d")
        
        self.pr_compra=float(input("Digite o preço de compra do album: "))
        self.tipo_compra=MeioFisico[input("Digite o tipo de compra (CD, VINIL, DOWNLOAD): ").upper()] 