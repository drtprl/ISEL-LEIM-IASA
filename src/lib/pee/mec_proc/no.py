class No:
    '''
        A classe No representa uma etapa de procura numa ávore de procura 
    contendo o estado atual, nó antecessor, o operador que gerou o estado atual
    e o custo acumulado até esta etapa.

        Foi realizado o override do método "less than" para comparar objetos 
    similares pelos seus atributos, neste caso pelo custo de cada nó.
    '''

    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        """
        Operador que gerou o nó corrente
        """
        return self.__operador
    
    @property
    def antecessor(self):
        return self.__antecessor
    
    @property
    def custo(self):
        """
        Soma do valor de cada operador até ao nó corrente.
        """
        return self.__custo
    
    @property
    def profundidade(self):
        """
        Níveis até chegar ao nó corrente.
        """
        return self.__profundidade
    
    def __init__(self, estado, operador = None, antecessor = None, custo = 0.0):
        self.__estado = estado # o qué é? aberto ou fechado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo
        if antecessor:
            self.__profundidade = antecessor.profundidade + 1
        else:
            self.__profundidade = 0

    def __lt__(self, other):
        '''
        Sobrescrevemos o método "less than" (__lt__) para comparar fácilmente 
        nós entre si.
        '''
        return self.__custo < other.custo