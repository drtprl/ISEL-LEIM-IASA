from ..mec_proc.procura_grafo import ProcuraGrafo
from .fronteira_fifo import FronteiraFIFO

class ProcuraLargura(ProcuraGrafo):

    def __init__(self):
        super().__init__(FronteiraFIFO())
