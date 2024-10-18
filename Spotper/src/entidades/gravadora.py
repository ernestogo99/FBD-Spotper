
class Gravadora:
    def __init__(self):
        self.nome=str(input("Digite o nome da gravadora: "))
        self.sede=str(input("Digite a sede da gravadora: "))
        self.home_pg=str(input("Digite a home page da gravadora: "))
        self.phones=[]
        
        quantidade=int(input("Digite a quantidade de telefones da gravadora: "))
        
        for i in range(0,quantidade):
            numero=str(input(f"digite o telefone {i+1} da gravadora: "))
            self.phones.append(numero)
            
   
        