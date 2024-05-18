from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):
    """A classe procura informada implementa o conceitos já heradados da 
    procura do melhor primeiro, a utilização de avaliadores. Estes avaliadores
    devem descrever a função de avaliação do custo da solução através de cada 
    nó gerado para serem ordenados de forma crescente segundo a sua prioridade
    na fronteira (Fronteira Prioridade).

    Por tanto, os métodos que derivem da procura informada devem definir uma 
    heurística para o cálculo que deve representar a estimativa de custo do 
    percurso desde o nó até ao objectivo, guiando a procura com fim de evitar
    realizar uma procura exaustiva no espaço de estados evidenciando o 
    conhecimento sobre o dominio do problema.

    Um exemplo com a vida real pode ser caminhar até um certo edifício que é
    reconhecivel no horizonte, porem não temos um mapa e não sabemos 
    qual pode ser a melhor escolha. Tudo aquilo que nós afaste do edificio 
    podemos considerar que não é o caminho certo. Este seria um exemplo prático
    de procura sôfrega com uma solução sub-óptima, porem conseguimos chegar na 
    mesma ao objectivo priorizando sómente o resto do caminho, pois para 
    realizar a procura A* deviamos considerar mais do que um percurso. 
    """
    def procurar(self, problema, heuristica):
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)