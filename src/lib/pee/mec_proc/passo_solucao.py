from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador

@dataclass
class PassoSolucao:
    """
    Esta é uma dataclass que define o operador para chegar ao passo.
    
    Uma data class é uma tipo de classe utilizada para armazenar dados de 
    maneira mais eficiênte definindo automáticamente métodos como o construtor
    ou geração do hash.

    Ao ser uma classe os atributos da propria podem ser consultados no formato
    passo.estado, mais fácil que no dicionario em que consultamos valores
    como dicionario['Key'], porem estes últimos são mais fáceis de indexar.
    """
    estado: Estado
    operador: Operador