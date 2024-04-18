class No:
    '''
    a classe No representa o nó de uma ávore de procura que
    contém o estado atual, estado antecessor e operador a
    realizar.
    Foi realizado o override do método "less than" para comparar
    objetos similares pelos seus atributos, neste caso o custo
    entre dois nós.
    '''

    @property
    def estado(self):
        return self.__estado
    @property
    def operador(self):
        return self.__operador
    @property
    def antecessor(self):
        return self.__antecessor
    @property
    def custo(self):
        return self.__custo
    @property
    def profundidade(self):
        return self.__profundidade
    
    def __init__(self, estado, operador = None, antecessor = None, custo = 0.0):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo
        if antecessor:
            self.__profundidade = antecessor.profundidade + 1
        else:
            self.__profundidade = 0

    def __lt__(self, other):
        return self.__custo < other.custo