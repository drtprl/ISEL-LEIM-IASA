from pee.mec_proc.fronteira import Fronteira
class FronteiraFIFO(Fronteira):
    '''
    Especialização da Fronteira de procura em largura.
    '''
    def inserir(self, no):
        self._nos.append(no)