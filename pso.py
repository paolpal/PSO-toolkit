import numpy as np
from problem import Problem
from particle import Particle

class PSO:
    def __init__(self, num_iterations, inertia_weight, c1, c2, num_particles=None, num_dimensions=None, problem=None, **kwargs):
        self.num_iterations = num_iterations
        if problem:
            self.problem = problem
        # Inizializza le particelle
        if num_particles:
            self.num_dimensions = num_dimensions
            self.num_particles = num_particles
            self.particles = [Particle(inertia_weight, c1, c2, num_dimensions, problem) for _ in range(num_particles)]

        # Inizializza la miglior posizione globale
            self.global_best_position = self.get_global_best_position()


    def get_global_best_particle(self):
        global_best_particle = min(self.particles, key=lambda particle: particle.fitness)
        return global_best_particle
     
    def get_global_best_position(self):
        # Trova la miglior posizione globale tra tutte le particelle
        global_best_particle = self.get_global_best_particle()
        return np.copy(global_best_particle.position)


    def update_particles(self):
        for particle in self.particles:
            # Aggiorna la velocità e la posizione della particella
            particle.update_velocity(self.global_best_position)
            particle.update_position()

            # Valuta la fitness della nuova posizione
            particle.evaluate_fitness(self.problem)

            # Aggiorna la miglior posizione personale e globale
            if particle.fitness < self.problem.evaluate(particle.best_position):
                particle.best_position = np.copy(particle.position)

            if particle.fitness < self.problem.evaluate(self.global_best_position):
                self.global_best_position = np.copy(particle.position)

    def run(self):
        for iteration in range(self.num_iterations):
            self.update_particles()

            # Opzionale: Puoi stampare la miglior fitness ad ogni iterazione
            print(f"Iteration {iteration + 1}, Best Fitness: {self.problem.evaluate(self.global_best_position)}")

        # Restituisci la miglior posizione globale alla fine delle iterazioni
        return self.global_best_position, self.problem.evaluate(self.global_best_position)


# Esempio di utilizzo
if __name__ == "__main__":
    num_particles = 30
    num_dimensions = 10
    num_iterations = 100
    inertia_weight = 0.5
    c1, c2 = 2.0, 2.0

    # Inizializza la classe del problema
    problem = Problem(num_dimensions)

    # Inizializza l'algoritmo PSO con la classe del problema
    pso = PSO(num_iterations, inertia_weight, c1, c2, num_particles, num_dimensions, problem)

    # Esegui l'algoritmo PSO
    best_position, best_fitness = pso.run()

    print("Best Position:", best_position)
    print("Best Fitness:", best_fitness)
