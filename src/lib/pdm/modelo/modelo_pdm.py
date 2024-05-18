from abc import ABC, abstractmethod

class ModeloPDM(ABC):
    """
    """
    @abstractmethod
    def S(self):
        ''''''

    @abstractmethod
    def A(self, s):
        ''''''

    @abstractmethod
    def T(self, s, a, sn):
        ''''''

    @abstractmethod
    def R(self, s, a, sn):
        ''''''
        
    @abstractmethod
    def suc(self, s, a):
        ''''''
