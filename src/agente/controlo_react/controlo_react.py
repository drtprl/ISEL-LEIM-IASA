from sae import Controlo
"""
Classe que implementa um controlo do agente baseado em
reações, temos um comportamento que tem associada uma accao e
no caso mais básico só devemos colocar a diraccao da Accao segundo
a direcao da percepcao. 
"""
class ControloReact(Controlo):

    def __init__(self, comportamento):
        '''
        mostrar_per_dir habilita a visualização da percepção
        direcional no simulador, informação que o agente guarda.
        '''
        self.__comportamento = comportamento
        self.mostrar_per_dir = True #Perceção direcional

    def processar(self, percepcao):
        """
        Activamos o proprio comportamento do controlo passando a 
        percepcao devolvendo uma ação.
        """
        return self.__comportamento.activar(percepcao)