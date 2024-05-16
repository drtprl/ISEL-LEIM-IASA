from mod_prob.problema_contagem import ProblemaContagem
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from mod_prob.heuristica_contagem import HeuristicaContagem
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.melhor_prim.procura_informada import ProcuraInformada

if __name__ == "__main__":
    VALOR_INICIAL = 0
    VALOR_FINAL = 9
    INCREMENTOS = [1, 2, -1]
    '''Definir o problema'''
    problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)
    '''Definir heurística'''
    heuristica = HeuristicaContagem(VALOR_FINAL)
    '''Definir o mecanismo de procura'''
    # Comentar o pop(0) da Fronteira IMPORTANTEEEEEE removemos o primeiro indice
    #mec_proc = ProcuraProfundidade()
    #mec_proc = ProcuraLargura() # Menos passos
    #mec_proc = ProcuraProfIter(10) # Procura em profundidade não vai ao infinito com incremento -1
    mec_proc = ProcuraCustoUnif() # Menor custo dando passos mais pequenos
    #mec_proc = ProcuraAA()
    #mec_proc = ProcuraSofrega()
    '''Resolver o problema'''
    #solucao = mec_proc.procurar(problema)
    solucao = mec_proc.procurar(problema, heuristica)

    print(f'Intervalo de {VALOR_INICIAL} até {VALOR_FINAL}')
    print('Custo: ', solucao.custo)
    print('Dimensão: ', solucao.dimensao)
    print('Passos até a solução:')
    for passo in solucao:
        # O valor do estado é o sucessor
        print(passo.estado.valor, passo.operador.incremento)