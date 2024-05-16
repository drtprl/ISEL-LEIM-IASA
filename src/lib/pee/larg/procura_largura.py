from ..mec_proc.procura_grafo import ProcuraGrafo
from .fronteira_fifo import FronteiraFIFO

class ProcuraLargura(ProcuraGrafo):
    """Breadth-First Search
    Procura em largura necessita implementar uma estrutura de informação em 
    grafos para facilitar a ordenada expansão dos seus nós, nível a nível. 
    
    Primeiramente, é iniciada uma fronteira FIFO para que este mecanismo de 
    procura possa colocar os nós expandidos no final da fronteira, assim
    estes só serão analizados por último e garantimos que não passamos de 
    nível sem analizar os adjacentes.

    Devemos ter atenção, pois vamos encontrar estados repetidos
    na árvore de procura. Este método de procura pode ser mais complexo 
    temporalmente que a procura em profundidade, para evitar analizar nó
    novamente, a procura em grafo (classe pai) tem uma lista com nós explorados
    indexados pelo valor do estado do nó, deste modo é mais fácil aceder ao 
    nó que pretendemos. 

    Concluimos que este algoritmo é tem uma complexidade computacional maior 
    que a procura em profundidade, porem é um mecanismo de procura completo, 
    pois se existir solução ela é encontrada, e óptimo porque a solução dada
    será sempre a melhor.
    """
    
    def __init__(self):
        super().__init__(FronteiraFIFO())
