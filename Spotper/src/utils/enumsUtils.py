from enums.enums import Periodo,Gravacao,MeioFisico



def check_periodo(prompt):
    while True:
        periodo_str = input(prompt).strip().lower()
        
        for periodo in Periodo:
            if periodo.value.lower() == periodo_str:
                return periodo.value

        print("Período inválido. Por favor, tente novamente.")
        
        
def check_meio_fisico(prompt):
    while True:
        meio_fisico=input(prompt).strip().upper()
        
        for meio in MeioFisico:
            if meio.value.upper()==meio_fisico:
                return meio.value
            
        print("Meio físico inválido, tente novamente. ")
   
   
   
def check_gravacao(prompt):
    while True:
        gravacao_type=input(prompt).strip().upper()
        
        for gravacao in Gravacao:
            if gravacao.value.upper()==gravacao_type:
                return gravacao.value
            
        print("Tipo de gravação inválida, tente novamente. ")     
        

