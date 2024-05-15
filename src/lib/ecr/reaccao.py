from .comportamento import Comportamento

class Reaccao(Comportamento):
    """A classe Reaccao representa o módulo que associa estímulo 
    a respota do controlo do agente reactivo que é um comportamento simples. 
    Com este nível de abstração do modelo de interação conseguimos 
    utilizar este código tanto num ambiente real como num ambiente
    virtual.

    A Reaccao especifica Comportemento pois o módulo comportamental está
    composto por comportamentos simples que por sua vez são reações. Recebemos
    estímulo que leva consigo a percepção. Finalmente, e através de um mecanismo
    de seleção de ação, geramos uma resposta, a acção selecionada.
    """
    def __init__(self, estimulo, resposta):
        """
        Construtor
        """
        self.__estimulo = estimulo
        self.__resposta = resposta

    
    def activar(self, percepcao):
        """
            Este método deteta a intensidade da percepcao e se o estímulo
            estiver presente, a resposta consegue produzir uma acção. 
            É utilizada a percepção como uma guarda para interferir na
            coerencia da resposta.

        Returns:
            Accao: resposta do sistema
        """
        
        intensidade =  self.__estimulo.detectar(percepcao)
        if intensidade>0:
            # A activação devolve uma accao trás ativar a resposta
            return self.__resposta.activar(percepcao, intensidade)