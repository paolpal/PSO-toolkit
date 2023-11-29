import numpy as np
from problem import ConvToE
from particle import PermutationParticle
from pso import PSO

import numpy as np

class Particle:
    def __init__(self, num_dimensions, num_objectives):
        self.position = np.random.rand(num_dimensions)
        self.velocity = np.random.rand(num_dimensions)
        self.best_position = np.copy(self.position)
        self.fitness = np.zeros(num_objectives)
        self.num_objectives = num_objectives

    def evaluate_fitness(self, objective_functions):
        self.fitness = np.array([obj_func(self.position) for obj_func in objective_functions])

    def update_velocity(self, global_best_position, inertia_weight, c1, c2):
        inertia_term = inertia_weight * self.velocity
        cognitive_term = c1 * np.random.rand() * (self.best_position - self.position)
        social_term = c2 * np.random.rand() * (global_best_position - self.position)

        self.velocity = inertia_term + cognitive_term + social_term

    def update_position(self):
        self.position = self.position + self.velocity

def pareto_dominance(particle1, particle2):
    # Implementazione della dominanza di Pareto
    return all(particle1_fitness <= particle2_fitness for particle1_fitness, particle2_fitness in zip(particle1.fitness, particle2.fitness))

def update_global_best(particles):
    # Aggiorna la miglior posizione globale in base alla dominanza di Pareto
    for i, particle_i in enumerate(particles):
        for j, particle_j in enumerate(particles):
            if i != j and pareto_dominance(particle_i, particle_j):
                particles[j].best_position = np.copy(particles[j].position)

def pso_multi_objective(objective_functions, num_particles, num_dimensions, num_iterations, inertia_weight, c1, c2):
    particles = [Particle(num_dimensions, len(objective_functions)) for _ in range(num_particles)]

    for iteration in range(num_iterations):
        for particle in particles:
            particle.evaluate_fitness(objective_functions)

        update_global_best(particles)

        for particle in particles:
            particle.update_velocity(get_global_best_position(particles), inertia_weight, c1, c2)
            particle.update_position()

    # Restituisci il fronte di Pareto approssimato
    pareto_front = [particle.position for particle in particles if is_pareto_optimal(particle, particles)]

    return pareto_front

def is_pareto_optimal(particle, particles):
    # Verifica se la particella è ottimale rispetto a tutte le altre
    return all(not pareto_dominance(p, particle) for p in particles if p != particle)

def get_global_best_position(particles):
    # Trova la miglior posizione globale rispetto al fronte di Pareto
    pareto_front = [particle.position for particle in particles if is_pareto_optimal(particle, particles)]
    global_best_position = min(pareto_front, key=lambda x: sum(x))
    return global_best_position

# Esempio di utilizzo
if __name__ == "__main__":
    def objective1(x):
        return x[0]

    def objective2(x):
        return 2 * x[1]

    objective_functions = [objective1, objective2]

    pareto_front = pso_multi_objective(
        objective_functions,
        num_particles=30,
        num_dimensions=2,
        num_iterations=100,
        inertia_weight=0.5,
        c1=2.0,
        c2=2.0
    )

    print("Pareto Front:", pareto_front)
