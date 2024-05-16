from abc import ABC, abstractmethod
class Fronteira(ABC):
    """
        Classe que representa o limite da árvore de procura onde temos a 
    fronteira de exploração para colocados os nós (estado atual + info do nó 
    antecessor + operadores que geraram esse estado) segundo o criterio de 
    ordenação que determine a estrategia de controlo de procura.

        A Fronteira é o recurso disponível para consultar os nós sucessores
    do nosso progresso de procura da solução. Esta deve ser iniciada com um
    dicionario de nós vazio para colocar o nó inicial no mecanismo de procura.

        Dependendo da mecanismo de procura, a nossa fronteira pode um criterio
    diferente de ordenação e de insersão no dicionario de nós. Foi estabelicido
    que o nó que deve ser analizado primeiro é o primeiro da lista para 
    posterior expansão da árvore de procura.
    """

    @property
    def vazia(self):
        return len(self._nos) == 0 

    def __init__(self):
        """ 
            Devemos iniciar a fronteira ao ser instanciada, para analizar se
        ela está vazia usamos o método vazia.
        """
        # 
        self.iniciar()
    
    def iniciar(self):
        self._nos = []
    
    @abstractmethod
    def inserir(self, no):
        ''''''

    def remover(self):
        """Devemos ter em atenção que vamos retirar o primeiro nó da lista de
        nós, na implementação da fronteira será importante na hora de escolher
        o método que coloque o nó na lista. 

        Uma fronteiraLIFO usa o método insert(0, nos) para colocar os nós 
        sucessores na primeira posição do [1,2,3] -> 4 -> [4,1,2,3] ao 
        contrario da fronteiraFIFO que colocar os nós na última posição
        [1,2,3] -> 4 -> [1,2,3,4]. Assim ao retirar com este método o nó a 
        expandir obtemos, sobre os exemplos anteriores, os seguintes resultados
        
        LIFO: _nos.pop(0) -> último nó em entrar -> 4[1,2,3]
        FIFO: _nos.pop(0) -> primeiro nó a entrar -> 1[2,3,4] 

        Returns:
            No: retiramos o nó da fronteira para expandira fronteira aplicando
            os operadores disponíveis no problema
        """
        return self._nos.pop(0)