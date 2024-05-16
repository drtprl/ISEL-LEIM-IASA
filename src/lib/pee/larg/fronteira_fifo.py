from pee.mec_proc.fronteira import Fronteira
class FronteiraFIFO(Fronteira):
    """A fronteira FIFO, firt in first out, especifica o críterio de inserção
    dos nós na fronteira de exploração, neste caso, inserimos os nós na 
    última posição da lista, para serem lidos os últimos pois o método remove 
    da classe fronteira faz pop(0) retirando da lista o primeiro elemento e
    garantindo que o nó inserido será removido por último para a expansão.
    """
    
    def inserir(self, no):
        self._nos.append(no)