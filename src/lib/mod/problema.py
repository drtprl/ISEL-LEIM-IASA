from abc import ABC, abstractmethod
class Problema(ABC):
    """Problema, representa o dominio do problema que é o estado inicial,
    o conjunto de operadores (custo), mais o objetivo que pode ser um
    estado o um conjunto de estados.

    Na inteligência artificial existe uma área que busca a resolução automática
    dos problemas por meio de algoritmos, o raciocínio automático. Este 
    raciocinio num sistema computacional precisa de um contexto mínimo,
    um modelo do problema, como o estado_inicial, os operadores para realizar
    ações dentro do domínio, e um ou vários objetivos para inferir numa solução
    beseada nesse conhecimento.

    Este conhecimento deve ser uma representação interna do sistema,
    codificando informação concreta do domínio do problema em estruturas
    simbólicas para posterior avaliação de opções,  sendo estás decodificadas
    em ações concretas.

    Na exploração de opções, devemos implementar um mecanismo de raciocinio, ou
    mecanismo de procura da resolução do problema, obtendo as opções possíveis
    através da simulação prospectiva para evaluar como se desenvolvem 
    diferentes eventos ou decisões ao longo do tempo. Nesta UC não serão 
    abordados modelos predictivos que simulam a evolução das variáveis 
    do ambiente.
    """

    @property
    def estado_inicial(self):
        """Configuração inicial do problema.

        Returns:
            Estado: propriedade do estado inicial do problema
        """
        return self.__estado_inicial
    
    @property
    def operadores(self):
        """Transformações possiveis dos estados perante ações.

        Returns:
            Operador[]: lista com os operadores internos do sistema.
        """
        return self.__operadores
    
    def __init__(self, estado_inicial, operadores):
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    @abstractmethod
    def objectivo(self, estado):
        """Método que compara o estado objectivo com o estado introduzido.

        Args:
            estado (Estado): estado a comparar com o estado objectivo.

        Returns:
            boolean: é ou não o estado objectivo?
        """