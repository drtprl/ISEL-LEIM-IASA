from ..resposta.resposta_mover import RespostaMover
from sae import Direccao
from random import choice

class RespostaEvitar(RespostaMover):

    def __init__(self, dir_inicial = Direccao.ESTE):
        self.__direccoes = list(Direccao)
        super().__init__(dir_inicial)

    def activar (self, percepcao, intensidade):
        contObst = percepcao.contacto_obst(percepcao.direccao)
        if(contObst):
            self._accao.direccao = self.__direccao_livre(percepcao)
        super().activar(percepcao, intensidade)

    def __direccao_livre(self, percepcao):
        # Observação: esqueci negar o if para devolver a primeira direccao livre
        direccoes_livres = [direccao for direccao in self.__direccoes 
                           if not percepcao.contacto_obst(direccao)]
        if direccoes_livres:
            return choice(direccoes_livres)
        
