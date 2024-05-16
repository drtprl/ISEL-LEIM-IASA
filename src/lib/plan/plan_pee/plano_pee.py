from ..plano import Plano

class PlanoPEE(Plano):
    '''
    
    '''

    def __init__(self, solucao):
        #self.__solucao = solucao #sequencia de passos
        self.__passos = [passo for passo in solucao]
    
    def obter_accao(self, estado):
        '''
        A solução é iterável
        1. verificar se existem passos
        2. se existir, buscamos o passo 
        Correção: com a primeira implementação o agente vai mais devagar
        pois estamos a fazer um for que devia ser feito noutro lado.
        '''
        '''
        self.__passos = [passo for passo in self.__passos]
        for passo in self.__passos:
            if passo.estado == estado:
                return passo.operador
        '''
        if self.__passos:
            passo = self.__passos.pop(0)
            if passo.estado == estado:
                return passo.operador
        
    
    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)