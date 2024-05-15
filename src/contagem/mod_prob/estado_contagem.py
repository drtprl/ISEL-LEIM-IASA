from mod.estado import Estado

class EstadoContagem(Estado):

    @property
    def valor(self):
        return self.__valor

    def __init__(self, valor):
        self.__valor = valor
    
    def id_valor(self):
        '''
        Se id for inteiro devolvemos um inteiro
        que é o valor
        A função hash do python já garante valores únicos
        para qualquer objeto.
        '''
        return hash(self.__valor)

