from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador

@dataclass
class PassoSolucao:
    '''Dataclass que define o operador para chegar a solução'''
    estado: Estado
    operador: Operador