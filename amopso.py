import numpy as np
from myproblems import ConvToE2
from particle import PermutationParticle
from mopso import MOPSO

class AMOPSO(MOPSO):
    def __init__(self, problem, num_particles, num_iterations, inertia_weight, c1, c2, preferred_obj=None, **kwargs):
        self.num_iterations = num_iterations
        self.problem = problem

        self.num_particles = num_particles
        self.particles = [PermutationParticle(inertia_weight, c1, c2, problem.n_var, problem) for _ in range(num_particles)]
        
        self.preferred_obj = preferred_obj
        self.global_best_position = self.get_global_best_position()

# Esempio di utilizzo
if __name__ == "__main__":
    num_particles = 20
    num_dimensions = 120
    num_iterations = 300
    inertia_weight = 0.3
    c1, c2 = .5, .9

    # Inizializza la classe del problema
    problem = ConvToE2(num_dimensions)

    # Inizializza l'algoritmo PSO con la classe del problema
    pso = AMOPSO(problem, num_particles, num_iterations, inertia_weight, c1, c2)

    # Esegui l'algoritmo PSO
    best_position, best_fitness = pso.run()

    print("Best Position:", best_position)
    print("Best Fitness:", best_fitness)