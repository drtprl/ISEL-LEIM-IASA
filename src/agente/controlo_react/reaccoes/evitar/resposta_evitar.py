from ..resposta.resposta_mover import RespostaMover
from sae import Direccao
from random import choice

class RespostaEvitar(RespostaMover):

    def __init__(self, dir_inicial = Direccao.ESTE):
        self.__direccoes = list(Direccao)
        super().__init__(dir_inicial)

    def activar (self, percepcao, intensidade):
        '''
        Método activar() verificar se existe algum obstaculo para poder evita-lo, verificando
        primeiramente a direccao da accao associada a resposta, caso seja haja um obstáculo 
        serão procuradas as direccoes livres e escolhida uma delas aleatoriamente.\n
        Este método implementa a alteração do estado interno do agente, a memória que pode inibir
        a entrada da nossa percepcao. Em conclusão, a resposta evitar tem a tarefa de virar o agente
        caso exista um obstáculo na direccao da direccao inicial.\n
        Obervações: 
        - Antes da entrega, coloquei como questão ao eng. 
        sobre qual devia ser a direccao mais adequada para utilizar no contacto_obst,
        mas por confusão o professor respondeu que devia ser percepcao.direccao e não
        self._accao.direccao associada a resposta.
        - Esqueci devolver a accao retornada pelo super().'''
        if percepcao.contacto_obst(self._accao.direccao):
            if direccao_livre := self.__direccao_livre(percepcao):
                self._accao.direccao = direccao_livre
            else:
                return None
        return super().activar(percepcao, intensidade)

    def __direccao_livre(self, percepcao):
        # Observação: esqueci negar o if para devolver a primeira direccao livre
        direccoes_livres = [direccao for direccao in self.__direccoes 
                           if not percepcao.contacto_obst(direccao)]
        if direccoes_livres:
            return choice(direccoes_livres)
        
