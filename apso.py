import numpy as np
from problem import ConvToE
from particle import PermutationParticle
from pso import PSO

class APSO(PSO):
    def __init__(self, num_iterations, inertia_weight, c1, c2, num_particles=None, num_dimensions=None, problem=None):
        super().__init__(num_iterations, inertia_weight, c1, c2)
        self.problem = problem
        self.num_particles = num_particles
        self.particles = [PermutationParticle(inertia_weight, c1, c2, num_dimensions, problem) for _ in range(num_particles)]
        self.global_best_position = self.get_global_best_position()

# Esempio di utilizzo
if __name__ == "__main__":
    num_particles = 40
    num_dimensions = 10
    num_iterations = 200
    inertia_weight = 0.5
    c1, c2 = 2.0, 2.0

    # Inizializza la classe del problema
    problem = ConvToE(num_dimensions)

    # Inizializza l'algoritmo PSO con la classe del problema
    pso = APSO(num_iterations, inertia_weight, c1, c2, num_particles, num_dimensions, problem)

    # Esegui l'algoritmo PSO
    best_position, best_fitness = pso.run()

    print("Best Position:", best_position)
    print("Best Fitness:", best_fitness)