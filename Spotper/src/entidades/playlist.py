from datetime import datetime

class Playlist:
    def __init__(self):
        self.nome=str(input("Digite o nome da playlist: "))
        self.dt_criacao=datetime.now()
        t_execução=input("digite o tempo de execução: HORA-MINUTO-SEGUNDO:")
        self.t_exec=datetime.strptime(t_execução,'%H:%M:%S').time()
        