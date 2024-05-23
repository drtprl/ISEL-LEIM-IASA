from plan.modelo.modelo_plan import ModeloPlan
from .modelo_pdm import ModeloPDM

class ModeloPDMPlan(ModeloPDM):
    """Satisfaz o modelo  das interfaces ModeloPlan e ModeloPDM para poder 
    injetar dependencias segundo as necessidades. Fatorização por delegação
    e não por herança.
    """
    @property
    def rmax(self):
        return self.__rmax
    
    @property
    def objectivos(self):
        return self.__objectivos
    
    def __init__(self, modelo_plan, objectivos, rmax = 1000.0):
        self.__modelo_plan = modelo_plan #delegamos a execução dos métodos
        self.__objectivos = objectivos
        self.__rmax = rmax # Recompensa máxima tanto pro ganho como para perda
                            # é simétrico
        # Realizamos o precalculo das transicoes para cada par estado/acção
        # para o nosso modelo determinista, as ações não tem probababilidades.
        self.__transicoes = {(s,a): a.aplicar(s) 
                             for s in self.obter_estados()
                             for a in self.obter_operadores()}

    def obter_estado(self):
        """Delegamos a obtenção do estado atual no modelo de plano."""
        return self.__modelo_plan.obter_estado()
    
    def obter_estados(self):
        """Delegamos a obtenção dos estados disponiveis"""
        return self.__modelo_plan.obter_estados()
    
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()

    def S(self):
        """Compaibilizamos os metodos com a interface"""
        return self.obter_estados()
    
    def A(self, s):
        """Devemos ter cuidado com os estados terminais que não têm ações.
        Para tal, devemos retornar os operadores"""
        return self.obter_operadores() if s not in self.__objectivos else [] 

    def T(self, s, a, sn):
        """Podemos ter um modelo determinista ou não determinista, no nosso
        caso implementaremos uma probabilidade de transição determinista, 
        a transição é garantida sendo um o valor a retornar.
        Na primeira expressão não é utilizado o valor sn, mas se quisermos 
        utilizar deve ser usado o modelo de transicao precalculado para 
        tratar de maneira mais eficiente a probabilidade de transição"""
        # return 1 if self.suc(s,a) else 0
        return 1 if self.__transicoes.get((s,a)) == sn else 0
        

    def R(self, s, a, sn):
        """Neste modelo não precisamos de nos preocupar com as colisões pois
        o modelo já trata das colisões, por tanto, só resta ao agente ir a 
        procura do obectivo """
        return self.__rmax if sn in self.__objectivos else -a.custo(s, sn)
        
    def suc(self, s, a):
        """Como o ambiente é determinista, aproveitamos que as transições
        foram precalculadas para aplicar o operador (acção) e devolver 
        um estado sucessor se ele existir."""
        sn = self.__transicoes.get((s,a))
        return [sn] if sn else []

    


