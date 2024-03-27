from ecr.comport_comp import ComportComp

class Prioridade(ComportComp):
    '''
    Prioridade, ou prioridade dinâmica, é um comportamento composto,
    um dos mecanismos de seleção de ação quando as ações interferem 
    entre si. A ação com maior prioridade é escolhida para execução.
    Esta comportamento depende de um estímulo para dar a prioridade.
    '''
    def seleccionar_accao(self, accoes):
        '''
        Este método caso existam ações, devolve a ação com maior prioridade
        '''
        if accoes:
            accao_sel = max(accoes, key=lambda accao: accao.prioridade)
            return accao_sel
