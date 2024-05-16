from abc import ABC, abstractmethod
class Estado(ABC):
    """Classe Estado representa com um identificador único, uma configuração 
    dentro do espaço de estados possiveis para a resolução de um problema.
    Exemplo: temos uma contagem de números inteiros de 
    1 a 4, o valor dos estados pode ser definido como o
    próprio valor do número.

    O estado compõem uma das partes do modelo do problema, é a estrutura 
    simbólica. Estes servem para realizar a exploração e avaliação de opções 
    para decisão acerca das melhores opções segundo a implementação das 
    técnicas de resolução de problemas.
    """

    @abstractmethod
    def id_valor():
        """Método a implementar que segundo o tipo de criterio a escolher para
        a identificação única do Estado, o seu valor que podera ser usado na
        escolha de opções.
        """
    
    def __hash__(self):
        """Sobre-escrevemos o método hash que todos os objetos tem por 
        definição para gerar uma nova função que coloca um valor único.

        Returns:
            valor: id valor do objecto Estado corrente.
        """
        return self.id_valor()
    
    def __eq__(self, other):
        """Método sobreescrito de python para comparar as identificações das
        instancias de uma determinada classe segundo o criterio escolhido.
        Neste caso, serão utilizados os valores hash que equivalem ao valor
        do proprio estado.

        Args:
            other (Estado): estado que será comparado com o atual

        Returns:
            boolean: são ou não o mesmo estado?
        """
        if isinstance(other, Estado):
            return self.__hash__() == other.__hash__()
