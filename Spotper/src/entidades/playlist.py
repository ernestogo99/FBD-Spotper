from datetime import datetime
from utils.timeUtils import input_time

class Playlist:
    def __init__(self):
        self.nome=str(input("Digite o nome da playlist: "))
        self.dt_criacao=datetime.now()
        self.t_exec=input_time("digite o tempo de execução: HORA:MINUTO:SEGUNDO: ")
        