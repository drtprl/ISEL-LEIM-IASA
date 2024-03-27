from ecr.comport_comp import ComportComp

class Hierarquia(ComportComp):
    '''
    Hierarquia é um comportamento composto, um dos mecanismos de seleção
    de ações de prioridades fixas de subsunção. Este comportamento não depende 
    de um estímulo para definir a sua prioridade, ela já esta definida.
    '''
    def seleccionar_accao(self, accoes):
        '''
        Ordem de hierarquia, o primeiro elemento é o de mais prioridade.
        '''
        if accoes:
            accao_sel = accoes[0]
            return accao_sel