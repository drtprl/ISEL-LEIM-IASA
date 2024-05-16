from pee.mec_proc.fronteira import Fronteira
class FronteiraLIFO(Fronteira):
    """A fronteira LIFO, last in first out, especifica o críterio de inserção
    dos nós na fronteira de exploração, neste caso, inserimos os nós na 
    primeira posição da lista. Caso não houver mais nada para explorar nesse
    ramo da árvore, simplesmente retrocedemos até poder continuar a explorar ou
    até encontrar o objectivo.

    Args:
        Fronteira: classe que representa a fronteira de exploração de uma 
    árvore de procura. 
    """

    def inserir(self, no):
        '''
        O nó a inserir será colocado na primeira posição
        '''
        self._nos.insert(0, no)