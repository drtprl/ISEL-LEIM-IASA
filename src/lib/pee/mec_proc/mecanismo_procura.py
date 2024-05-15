from abc import ABC, abstractmethod
from .no import No
from .solucao import Solucao
class MecanismoProcura(ABC):
    '''
    
    '''

    def __init__(self, fronteira):
        self._fronteira = fronteira

    def _iniciar_memoria(self):
        self._fronteira.iniciar()
    
    @abstractmethod
    def _memorizar(self, no):
        '''
        
        '''
    
    def procurar(self, problema):
        '''
        Procura a solucao
        '''
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        # Memoria iniciada com o estado inicial guardado
        self._memorizar(no)
        while not self._fronteira.vazia:
            no = self._fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)
            for no_sucessor in self._expandir(problema, no):
                # Memorizar inclui o inserir, 
                # utiliza o inserir conveniente
                self._memorizar(no_sucessor)
    
    def _expandir(self, problema, no):
        sucessores = []
        estado = no.estado
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado)
            if estado_suc is not None:
                custo = no.custo + operador.custo(estado, estado_suc)
                # no aqui se refere ao no anterior
                no_sucessor = No(estado_suc, operador, no, custo)
                sucessores.append(no_sucessor)
        return sucessores
