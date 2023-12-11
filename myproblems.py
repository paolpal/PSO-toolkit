import numpy as np
from .algebric import *
from .problem import MOProblem, Problem

class Schaffer1(MOProblem):
    def __init__(self):
        # Chiamiamo il costruttore della classe base con n_obj = 2
        super().__init__(n_var=1, n_obj=2)

    def evaluate(self, position):
        # Implementa la tua funzione di valutazione multi-obiettivo
        # Questo è il posto dove valuti quanto è buona la soluzione corrente
        obj1 = position[0]**2  # Esempio di valutazione per il primo obiettivo
        obj2 = (position[0]-2)**2  # Esempio di valutazione per il secondo obiettivo

        return [obj1, obj2]

class ConvToE(Problem):
    def evaluate(self, position):
        e = list(range(1, len(position)+1))
        dif = sub(position,e)
        s = randbs_decomposition(dif)
        return len(s)**2
    

class ConvToE2(MOProblem):
    def __init__(self, n_var):
        # Chiamiamo il costruttore della classe base con n_obj = 2
        super().__init__(n_var=n_var, n_obj=1)

    def evaluate(self, position):
        e = list(range(1, len(position)+1))
        dif = sub(position,e)
        s = randbs_decomposition(dif)
        return [len(s)**2]


