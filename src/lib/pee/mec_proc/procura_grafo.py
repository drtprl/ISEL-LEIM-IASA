from .mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura):
    '''
    Por definição um grafo é um diagrama que representa mediante pontos e 
    linhas as relações entre pares de elementos para resolver problemas de 
    carater lógico, topológico ou de cálculo combinatorio. Nesta UC,
    as classes que herdem de procura grafo vão poder ajudar-se da lista de nós
    explorados. Ao expandir um nó aberto, ele fica como explorado.

    Por tanto, na fronteira usada nas classe derivadas de procuraGrafo sempre 
    vamos retroceder ao sucessor até não haver mais operadores disponiveis.
    Os explorados ficam indexados num dicionario segundo o estado (único)
    atribuido a cada nó.

    No outro lado, a procura em profundidade não necessira da procura 
    em grafo porque utiliza a pilha de dados na fronteira LIFO, last in first 
    out, explorando tão profundo quanto possível antes de exploram ramo 
    adjacente.
    '''
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {} # Iniciar um dicionario

    def _memorizar(self, no):
        """Só inserimos um nó na fronteira se ele não foi explorado,
        """
        estado = no.estado
        if self._manter(no):
            self._fronteira.inserir(no)
            #print("Estado memorizado:",estado.valor)
            self._explorados[estado] = no

    def _manter(self, no):
        '''
        Para evitar acumular um nó já explorado,
        devolvemos false para não memorizar nem na fronteira, 
        nem nos explorados.
        '''
        return no.estado not in self._explorados