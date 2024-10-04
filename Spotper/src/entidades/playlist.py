from datetime import datetime

class Playlist:
    def __init__(self):
        self.nome=str(input("Digite o nome da playlist: "))
        self.dt_criacao=datetime.now()
        self.t_exec=datetime.strptime("00:00:00",'%H:%M:%S')
        