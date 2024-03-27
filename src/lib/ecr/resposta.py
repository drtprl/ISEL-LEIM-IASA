class Resposta:
    """
    Esta classe faz parte da reação(estímulo-resposta). 
    Após detetar a intensidade do estímulo usamos a 
    guarda da percepção para identificar se houve percepcao,
    caso sim, devolver a ação correspondente que será a classe
    Reaccao a devolver ao ambiente.
    Modulo ecr: esquemas comportamentais reativos
    """
    def __init__(self, accao):
        self._accao = accao

    def activar(self, percepcao, intensidade=0.0):
        """
        Ao ativar a nossa resposta usamos a guarda da percepcao e 
        colocamos o a prioridade da accao com a intensidade antes
        de retornar.
        Parameters:
            percepcao(Percepcao) - vinda do ambiente
            intensidade(float) - intensidade do estímulo

        Returns:
            accao(Accao) : accao associada a resposta.
        """
        if percepcao is not None:
            self._accao.prioridade = intensidade
            return self._accao