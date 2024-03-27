from .comportamento import Comportamento

class Reaccao(Comportamento):
    """
    A classe Reaccao representa a associação Estímulo-Resposta do controlo
    reactivo que é um comportamento simples. 
    Com este nível de abstração do modelo de interação conseguimos 
    utilizar este código tanto num ambiente real como num ambiente
    virtual. 
    Modulo ecr: esquemas comportamentais reativos
    """
    def __init__(self, estimulo, resposta):
        """
        Construtor
        """
        self.__estimulo = estimulo
        self.__resposta = resposta

    
    def activar(self, percepcao):
        """
        Método que activa a percepção do ambiente caso a intensidade do
        estímulo seja maior que zero.

        Returns:
            accao (Accao): resposta do sistema
        """
        intensidade = self.__estimulo.detectar(percepcao)
        if(intensidade>0):
            # A activação devolve uma accao
            return self.__resposta.activar(percepcao, intensidade)