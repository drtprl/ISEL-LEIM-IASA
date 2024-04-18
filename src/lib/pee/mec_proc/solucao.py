from .passo_solucao import PassoSolucao
class Solucao:
    '''
    Classe Solucao concretiza o problema, ficam guardadas os atributos
    do espaço de estados e do problema que satisfazem o tipo de procura
    desejada.
    '''

    @property
    def dimensao(self):
        return self.__no_final.profundidade
    
    @property
    def custo(self):
        return self.__no_final.custo
    
    def __iter__(self):
        '''Assim tornamos este objeto em iterável'''
        return iter(self.__passos)
    
    def __getitem__(self, index):
        '''Tornamos o objeto indexável, exemplo: 
        passo_solucao = solucao[1]\n
        Assim acedemos aos passos da solucao segundo o indice.
        '''
        return self.__passos[index]
    
    def __init__(self, no_final):
        self.__no_final = no_final
        self.__passos = []
        no = no_final
        while no.antecessor:
            # Operador ao estado atual, o estado ao antecessor
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0,passo)
            no = no.antecessor
    
