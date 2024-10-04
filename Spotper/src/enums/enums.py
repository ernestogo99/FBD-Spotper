from enum import Enum

class MeioFisico(Enum):
    CD="CD"
    VINIL="VINIL"
    DOWNLOAD="DOWNLOAD"
    
class Gravacao(Enum):
    ADD='ADD'
    DDD='DDD'

class Periodo(Enum):
    IDADE_MEDIA = "idade média"
    RENASCENCA = "renascença"
    BARROCO = "barroco"
    CLASSICO = "clássico"
    ROMANTICO = "romântico"
    MODERNO = "moderno"
    