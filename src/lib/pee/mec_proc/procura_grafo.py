from .mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura):
    '''
    Qual o critério para manter um no na fronteira segundo o custo
    '''
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {} # Iniciar um dicionario

    def _memorizar(self, no):
        estado = no.estado
        if self._manter(no):
            self._fronteira.inserir(no)
            self._explorados[estado] = no

    def _manter(self, no):
        '''
        Para evitar analizar un ramo com maior custo, se este já foi explorado
        devolvemos false para não memorizar na fronteira nem nos explorados.
        '''
        return no.estado not in self._explorados