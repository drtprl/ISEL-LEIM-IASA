from pee.mec_proc.fronteira import Fronteira
class FronteiraLIFO(Fronteira):
    '''
    Especialização da Fronteira de procura em profundidade.
    '''

    def inserir(self, no):
        '''
        O nó a inserir será colocado na primeira posição
        '''
        self._nos.insert(0, no)