import numpy as np
import algebric

class Problem:
    def __init__(self, num_dimensions):
        self.num_dimensions = num_dimensions

    def evaluate(self, position):
        # Implementa la tua funzione di fitness specifica del problema
        # Questo è il posto dove valuti quanto è buona la soluzione corrente
        return np.sum(position)  # Esempio di fitness, sostituisci con la tua logica

class ConvToE(Problem):
    def evaluate(self, position):
        e = list(range(1, len(position)+1))
        dif = algebric.sub(position,e)
        s = algebric.randbs_decomposition(dif)
        return len(s)**2
