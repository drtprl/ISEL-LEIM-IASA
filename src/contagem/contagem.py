from mod_prob.problema_contagem import ProblemaContagem
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_prof_iter import ProcuraProfIter

if __name__ == "__main__":
    VALOR_INICIAL = 0
    VALOR_FINAL = 9
    INCREMENTOS = [1, 2, -1]
    #Definir o problema 
    problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)
    #Definir o mecanismo de procura
    #mec_proc = ProcuraProfundidade()
    mec_proc = ProcuraLargura()
    #mec_proc = ProcuraProfIter(10) # Procura em profundidade não vai ao infinito com incremento -1
    #Resolver o problema
    solucao = mec_proc.procurar(problema)

    print('Valor inicial:', VALOR_INICIAL)
    print('Valor Final:', VALOR_FINAL)
    print('Incrementos:', INCREMENTOS)
    print('Passos até a solução:')
    for passo in solucao:
        # O valor do estado é o sucessor
        print(passo.estado.valor, passo.operador.incremento)