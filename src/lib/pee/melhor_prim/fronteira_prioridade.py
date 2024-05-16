from pee.mec_proc.fronteira import Fronteira
from heapq import heappush, heappop

class FronteiraPrioridade(Fronteira):
    '''
    
    '''
    def __init__(self, avaliador):
        '''

        '''
        self.__avaliador = avaliador
        super().__init__()

    def inserir(self, no):
        '''
        Inserimos um elemento segundo prioridade com
        a ferramenta heapq que ordena automáticamente
        os elementos da lista.
        O calculo da prioridade é tarefa do avaliador.
        '''
        prioridade = self.__avaliador.prioridade(no)
        # estrutura do heappush: estrutura de dados alvo + tuplo com prioridade do no e no
        heappush(self._nos, (prioridade, no))
    
    def remover(self):
        '''Retiramos o tuplo com maior prioridade.\n
        Usamos variavel anónima para ignorar o valor da prioridade e 
        podemos retirar os () porque em python quaisquer valores
        seguidos de uma vírgula é um tuplo.\n
        Variaveis anónimas proporcionam clareza ao código.\n
        -, no vs no = heappop(wtv)[1]'''
        _, no = heappop(self._nos)
        return no