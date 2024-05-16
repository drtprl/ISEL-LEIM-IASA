from .passo_solucao import PassoSolucao
class Solucao:
    '''
    Classe Solucao concretiza o problema, ficam guardadas os atributos
    do espaço de estados e do problema que satisfazem o tipo de procura
    desejada. A solução armazena uma solução encontrada pelo mecanismo 
    de procura, os passos a seguir para chegar ao objectivo junto de outros
    parâmetros interessantes como a dimensão da solução (numero de passos) e
    o custo desta soluçao que pode não ser óptima.
    '''

    @property
    def dimensao(self):
        """
            Propriedade que define o nível do nó corrente na árvore árvore de
        exploração. 
        """
        return self.__no_final.profundidade
    
    @property
    def custo(self):
        """
            Custo da solução calculado através do acumulação de recursos
        necessários para chegar ao nó final equivalente ao objectivo do 
        problema.
        """
        return self.__no_final.custo
    
    def __iter__(self):
        '''Assim tornamos este objeto em iterável usando os passos da solução
    como alvo.'''
        return iter(self.__passos)
    
    def __getitem__(self, index):
        '''Tornamos o objeto indexável, exemplo: 
        passo_solucao = solucao[1]\n
        Assim acedemos aos passos da solucao segundo o indice.
        '''
        return self.__passos[index]
    
    def __init__(self, no_final):
        """O construtor da solução guarda o nó final, o objectivo, e guarda os
        nós até a solução. Os nós de caminho até a nó final serão armazenados 
        como PassoSolucao, data class para facil manuseamento dos dados, 
        podemos facilmente iterar este objeto sem a necessidade de criar ou
        sobre escrever um método adicional e.g.

        O passo solução só inclui a informação do estado do antecessor e do 
        operador do proprio. 

        Args:
            no_final (No): Nó solução do problema
        """
        self.__no_final = no_final
        self.__passos = []
        no = no_final
        while no.antecessor:
            # Operador ao estado atual, o estado ao antecessor
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0,passo)
            no = no.antecessor
    
