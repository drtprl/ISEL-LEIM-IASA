from sae import Agente, Simulador
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from controlo_delib.controlo_delib import ControloDelib

class AgenteDelibPDM(Agente):
    """O gamma definido por defeito é muito baixo e por isso no simulador 4
    é necessário colocar, por exemplo, gama = 0.98"""
    def __init__(self):
        planeador = PlaneadorPDM(gama = 0.98)
        controlo = ControloDelib(planeador)
        super().__init__(controlo)

if __name__ == "__main__":
    Simulador(4, AgenteDelibPDM()).executar()