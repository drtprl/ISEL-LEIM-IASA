from agente.controlo_react.reaccoes.recolher import Recolher
from sae import Agente, Simulador
from agente.controlo_react.controlo_react import ControloReact

class AgenteReactivo(Agente):
    def __init__(self):
        comportamento = Recolher()
        controlo = ControloReact(comportamento)
        super().__init__(controlo)

# Executar a simulação
if __name__ == "__main__":
    Simulador(4, AgenteReactivo()).executar()

