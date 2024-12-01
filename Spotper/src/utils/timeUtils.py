from datetime import datetime

def input_data(prompt):
        while True:
            try:
                data_str = input(prompt)
                return datetime.strptime(data_str, "%Y-%m-%d").date()
            except ValueError:
                print("Formato de data inválido. Tente novamente.")
                

def input_time(prompt):
    while True:
        try:
            time_str=(input(prompt))
            return datetime.strptime(time_str,"%H:%M:%S").time()
        except ValueError:
            print("Formato de tempo inválido, Tente novamente.")
            
def formatar_interv_tempo(inicio, fim):
        return f"[{inicio},{fim}]"