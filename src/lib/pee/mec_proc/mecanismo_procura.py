from abc import ABC, abstractmethod
from .no import No
from .solucao import Solucao

class MecanismoProcura(ABC):
    """
    Os mecanismo de raciocinio através da procura são uma das formas mais 
    elementares de resolver problemas. Neste caso, os mecanismos de procura, 
    devem implementar os conceitos do modelo do problema. No raciocinio 
    automático, representamos o dominio do problema com um espaço de estados. 
    
    O mecanismo de procura tem como função principal encontrar uma solução ao 
    problema de planeamento para resolve-lo. Cada transição gera uma estado 
    novo a junção dos passos cria um ou vários percurso ou varios até ao 
    objectivo. Segundo utilizando um ou outro critério de avalição de opções,
    pode ser escolhido um dos percursos segundo o custo (normalmente, buscamos
    mínimizar o custo) ou o valor (usualmente, procuramos maximizar ganhos
    e minimizar as perdas).

    No espaço de soluções podemos produzir soluções óptimas ou subóptimas. 
    Segundo o tipo de mecanismo de procura. Também, podemos ter métodos de
    procura não informada ou informada com acesso ao contexto de todo o 
    problema, estes últimos podem ser mais eficientes.

    Qualquer classe que derive de MecanismoProcura deve manter a informação em
    cada passo de procura numa árvore de procura (grafo de espaço de estados) 
    onde cada estado inclui a informação do relativa a cada transição, deve
    aplicar a procura da solução expandir a fronteira de exploração. 
    
    No limite da árvore de procura temos a fronteira de exploração onde serão 
    colocados os nós (estado atual + info do nó antecessor + operadores que 
    geraram esse estado) segundo um criterio de ordenação que determine a 
    estrategia de controlo de procura.
    """

    def __init__(self, fronteira):
        self._fronteira = fronteira

    def _iniciar_memoria(self):
        if not self._fronteira.vazia:
            self._fronteira.iniciar()
    
    def procurar(self, problema):
        """
            Este método implementa a procura da solução do nosso método de 
        procura usufruindo dos métodos memorizar e expandir. 

            No ciclo de funcionamento do método podemos observar que devemos 
        iniciar uma fronteira, por norma uma fronteira de exploração vazia.
        De seguida, acudimos ao problema para obter o estado inicial e coloca-
        lo na fronteira para iniciar a exploração no espaço de estados 
        expandindo a fronteira até encontrar uma solução ou não caso a 
        fronteira fique vazia.  

            Ao memorizar um nó com na fronteira LIFO é inserido diretamente,
        na fronteira FIFO ele é analizado pegando no estado para identificar 
        se já existe na lista de explorados. Sempre que analizamos um nó 
        devemos retiralo da primeira posição da fronteira, expandir para 
        encontrar os sucessores e pedir ao método _memorizar de uma das 
        especificações de mecanismo de procura que memorize, ou não, segundo o 
        seu criterio.

            Um mecanismo de procura pode ser óptimo, pois é a solução 
        encontrada é a melhor das várias possíveis, ou completo, onde este
        garante que, caso exista solução, esta será encontrada.

        Args:
            problema (Problema): problema que queremos resolver

        Returns:
            Solucao: retornamos a primeira solução gerada pelo mecanismo de 
        procura.
        """
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
    
    @abstractmethod
    def _memorizar(self, no):
        """
            Método a implementa o criterio de colocação e ordenação dos nós na 
        fronteira de exploração da árvore de procura dependendo do tipo de 
        procura.
        """
    
    def _expandir(self, problema, no):
        """
            Este método fica encarrego por aplicar os operadores possíveis no
            problema para econtrar os nós sucessores no seguinte nível de 
            procura. Também, é calculado o custo acumulado de cada nó sucessor. 

        Args:
            problema (Problema): problema ao que queremos achar solução
            no (No): configuração que mantem a informação desse ponto na árvora
            de exploração.

        Returns:
            List<No>: nós sucessores após aplicar os operadores disponíveis
        """
        sucessores = []
        estado = no.estado
        for operador in problema.operadores:
            #print("Operador",operador)
            estado_suc = operador.aplicar(estado)
            if estado_suc is not None:
                custo = no.custo + operador.custo(estado, estado_suc)
                # no aqui se refere ao no anterior
                no_sucessor = No(estado_suc, operador, no, custo)
                sucessores.append(no_sucessor)
        return sucessores
