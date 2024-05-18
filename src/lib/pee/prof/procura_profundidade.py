from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):
    """Depth-first search - DFS:
    A classe ProcuraProfundidade deve especificar a maneira de inserir os 
    dados no array de nós, para isso é utilizada uma instancia da fronteira
    LIFO onde armazenamos nós a medida que expandimos o primero nó de cada 
    nível de busca. Este método de procura não é óptimo, pois podemos não 
    encontrar solução, nem completo porque a solução encontrada, o percurso,
    pode não ser o melhor das opções. Este algoritmo é interessante pois a sua
    complexidade espacial é baixa, pois a exploraçao do espaço pode ser muito 
    menor que a procura em largura, ocupando menos memoria.
    
    O caminho de exploração formado ao longo do tempo é um 
    ramo da árvore de exploração, obtendo com este algoritmo de busca 
    não-informada uma complixade espacial menor que o algoritmo de busca em 
    largura. A complexidade temporal de ambos é proporcional ao número de 
    estados que são explorados.
    
    A fronteira  vai adicionando os nós, caso não haja mais onde explorar, 
    é retrocedido um nível "backtrack", e é usado o seguinte operador 
    disponível do nó antecessor.

    Surge um problema, pois no caso de existir uma profunidade muito grande a 
    busca pode chegar a ser infinita, chegando a esgotar a memoria disponível. 
    A solução não passa por marcar os nós explorados como na procura em largura
    , mas sim estabelecer um limite na profundidade de busca.

    No exemplo dado em aula, ao colocar um -1 no primeiro lugar da lista de 
    operadores vamos encontrar uma contagem decrescente. O estado ira sempre
    em regrassão sem nunca chegar ao objectivo, mas sim afastar-se cada vez
    mais. A solução é colocar uma profundidade limite para explorar outros nós 
    ao chegar na profundidade limite desse ramo da árvore. 
    
    Mais a frente, colocar um limite continua ocupando muita memoria e nesse 
    caso faremos uma procura em profundidade iterativa que explora 
    iterativamente cada nível, mais parecido com a profundidade em largura.

    exemplo gráfico:
      0
     /|\\
    1 2 -1
         /|\\
       0 1 -2
            /|\\
         -1 0 -3
               /|\\
            -2-1-4

    Args:
        MecanismoProcura: classe abstrata a qual será provista de conteúdo.
    """
    def __init__(self):
        '''
        Iniciamos a fronteira pretendida
        '''
        super().__init__(FronteiraLIFO())

    def _memorizar(self, no):
        '''
        Memorizamos o nó pretendido com a lógica de ordenação da FronteiraLIFO.
        '''
        #print(no.estado.valor)
        self._fronteira.inserir(no)