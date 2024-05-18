from pee.mec_proc.procura_grafo import ProcuraGrafo
from .fronteira_prioridade import FronteiraPrioridade
class ProcuraMelhorPrim(ProcuraGrafo):
    '''
    Procura do melhor primeiro, Best-First, é um tipo de algoritmo que utiliza
    uma função "f" para avaliar cada nó "n" gerado, essa avaliação será feita
    com a classe Avaliador passada como argumento no construtor deste método
    de procura.

    Podemos calcular o custo da função de três maneiras ao realizar a busca do 
    melhor primeiro sobre o espaço de estados. A primeira é colocar a 
    prioridade dos nós segundo o custo dos nós explorados, segunda calculando a
    prioridade através da estimativa do custo por meio de uma função heurística
    com a procura sôfrega, e por último, juntandos os dois casos para obter a 
    busca A*

    Temos f(n)>=0, função avaliadora, que usualmente representa uma estimativa 
    do custo da solução através do nó "n". O que se pretende é minimizar o 
    custo, para isso os nós são analizados em ordem crescente de f(n), quanto 
    maior o custo, mais no final da fronteira será colocados o nó não fechado.
    
    Se estivermos perante um método de procura não informado, como a procura
    de custo uniforme, não será utilizada uma heurística na função f(n) onde
    só vamos encontrar o custo dos nós explorados fazendo uma busca não guiada
    da solução sobre todo o espaço de estados. f(n) = g(n) (custo do percurso
    até n)

    Perante um método de procura informada, faremos uso de heurísticas que 
    reflete o conhecimento acerca do dominio do problema para ordenar a 
    fronteira de exploração, ficando uma função f(n)=h(n)(Procura sôfrega) ou
    f(n)=g(h)+h(n)(Procura A*). A heurística faz uma estimativa do custo de o 
    nó até ao objectivo sem que o percurso tenha sido explorado. na procura A*
    obtemos uma solução optima, porem temos uma complexidade maior que na
    procura sôfrega, que é uma solução sub-óptima.

    O método manter deve garantir que o nó que vamos colocar na fronteira não
    esteja na lista de explorados ou que no caso de estar, o custo acumulado 
    do caminho que gerou esse nó seja menor que o nó com o mesmo estado dentro
    da lista de explorados.

    A procura do melhor-primeiro é uma estrategia de busca heurística onde 
    tentamos minimizar o custo da solução explorando primeiro os nós que 
    parecem mais vantajosos a diferença da procura em largura que explora os 
    todos os níveis segundo a ordem pre-estabelecida dos operadores. Deste modo
    podemos concluir que o algoritmo Best-First, a priori, tem menor 
    complexidade espacial que o algoritmo Breadth-First (largura), mas continua
    tendo maior complexidade temporal que o algoritmo Depth-First (profundidade
    ), a menos que este não encontre uma solução, e dependendo do problema, 
    deve ser escolhido outro mecanismo de procura diferente ao de profundidade.
    '''
    def __init__(self, avaliador):
        fronteira  = FronteiraPrioridade(avaliador)
        super().__init__(fronteira)
        self._avaliador = avaliador

    def _manter(self, no):
        '''
        Mantemos o no se existir nos explorados do super
        ou se tiver custo menor que o no com o mesmo estado
        nos explorados. Relembrar que estamos a comparar custo
        já calculado na funcao __lt__ do nó
        '''
        return super()._manter(no) or \
            no < self._explorados[no.estado] 

