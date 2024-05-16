from ..planeador import Planeador
from pee.melhor_prim.procura_aa import ProcuraAA
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from .plano_pee import PlanoPEE

class PlaneadorPEE(Planeador):
    '''
    Este planeador utiliza a função h da procura A*
    que procura 
    '''
    def __init__(self):
        self.__mec_proc = ProcuraAA()
        
    def planear(self, modelo_plan, objectivos):
        '''
        Consideramos que a lista de objectivos vem ordenada, por tanto,
        o mais prioritario é o primeiro.
        Correção: não tinha verificado se havia objectivos
        '''
        if objectivos:
            estado_final = objectivos[0]
            problema = ProblemaPlan(modelo_plan, estado_final)
            heuristica = HeurDist(estado_final)
            solucao = self.__mec_proc.procurar(problema, heuristica)
            if solucao:
                return PlanoPEE(solucao)
        