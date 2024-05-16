from abc import ABC, abstractmethod
class Operador(ABC):
    """Classe Operador representa as varias ações que provocam
    uma transição de estado. Operadores só podem ser representações internas de 
    estado como fazer uma translação de um objeto no eixo cartesiano através de
    somas ou junção de símbolos para formar palavra concretas, ou seja, 
    transições que geram estados novos.

    Qualquer classe derivada de Operador deve, no mínimo, gerar a transformação
    e calcular os custos dessa operação, os recursos necessários para gerar o
    novo estado.
    """
    
    @abstractmethod
    def aplicar(self, estado):
        """Método que gera um novo estado

        Args:
            estado (Estado): estado atual
        Returns:
            Estado
        """
    
    @abstractmethod
    def custo(self, estado, estado_suc):
        """Método que calcula o gasto realizado para transicionar
        entre o estado atual e sucessor.

        Args:
            estado (Estado): estado atual
            estado_suc (Estado): estado sucessor

        Returns:
            double: resultado do calculo dos recurso utilizados para realizar
            a transição
        """