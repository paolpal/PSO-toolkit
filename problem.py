import numpy as np

class Problem:

    def __init__(self, n_var):
        self.n_var = n_var


    def evaluate(self, position):
        # Implementa la tua funzione di fitness specifica del problema
        # Questo è il posto dove valuti quanto è buona la soluzione corrente
        return np.sum(position)  # Esempio di fitness, sostituisci con la tua logica


class MOProblem(Problem):
    def __init__(self, n_var, n_obj):
        super().__init__(n_var)
        self.n_obj = n_obj
