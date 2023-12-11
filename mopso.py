import numpy as np
import copy
import random

from .particle import Particle
from .pso import PSO

class MOPSO(PSO):
    def __init__(self, problem, num_particles, num_iterations, inertia_weight, c1, c2, preferred_obj=None, **kwargs):
        self.num_iterations = num_iterations
        self.problem = problem
        # Inizializza le particelle
        self.num_particles = num_particles
        self.particles = [Particle(inertia_weight, c1, c2, problem.n_var , problem) for _ in range(num_particles)]
            
        # Inizializza la miglior posizione globale
        self.preferred_obj = preferred_obj
        self.global_best_position = self.get_global_best_position()
    
    def dominate(self, x_obj, y_obj):
        """
        Valuta la dominanza di Pareto tra due soluzioni.

        Parameters:
        - x_obj: Lista di valori della soluzione 1
        - y_obj: Lista di valori della soluzione 2

        Returns:
        - True se x_obj domina y_obj, False altrimenti
        """
        dominates = False
        for i in range(self.problem.n_obj):
            if x_obj[i] < y_obj[i]:
                dominates = True
            elif x_obj[i] > y_obj[i]:
                return False  # Solution_a non domina solution_b su almeno un obiettivo
        return dominates
    
    def better(self, x_obj, y_obj):
        if self.preferred_obj:
            return x_obj[self.preferred_obj] < y_obj[self.preferred_obj]
        else:
            return random.choice([True, False])
    
    def get_global_best_position(self):
        global_best_position = self.particles[0].best_position
        #global_best_fitness = self.problem.evaluate(self.particles[0].best_position)
        global_best_fitness = self.particles[0].best_fitness
        for particle in self.particles[1:]:
            #particle.best_fitness = self.problem.evaluate(particle.best_position)
            if self.dominate(particle.best_fitness, global_best_fitness):
                global_best_position = copy.deepcopy(particle.best_position)
                global_best_fitness = particle.best_fitness.copy()
            elif not self.dominate(global_best_fitness, particle.best_fitness):
                if self.better(particle.best_fitness, global_best_fitness):
                    global_best_position = copy.deepcopy(particle.best_position)
                    global_best_fitness = particle.best_fitness.copy()
        return global_best_position
    
    def closer_to_origin(self, x_obj, y_obj):
        # Calcola la distanza dall'origine per entrambi i vettori
        x_dist = np.linalg.norm(x_obj)
        y_dist = np.linalg.norm(y_obj)

        # Restituisci True se il primo vettore è più vicino in modulo all'origine
        return x_dist < y_dist

    def update_particles(self):
        for particle in self.particles:
            # Aggiorna la velocità e la posizione della particella
            particle.update_velocity(self.global_best_position)
            particle.update_position()

            # Valuta la fitness della nuova posizione
            particle.evaluate_fitness(self.problem)

            # Aggiorna la miglior posizione personale e globale
            #particle.best_fitness = self.problem.evaluate(particle.best_position)
            if self.dominate(particle.fitness, particle.best_fitness):
                particle.best_position = np.copy(particle.position)
                particle.best_fitness = particle.fitness.copy()
            elif not self.dominate(particle.best_fitness, particle.fitness):
                if self.closer_to_origin(particle.fitness, particle.best_fitness):
                    particle.best_position = copy.deepcopy(particle.position)
                    particle.best_fitness = particle.fitness.copy()

        self.global_best_position = self.get_global_best_position()        


        # MOPSO ISSUES
        # L'algoritmo non converge. (?)
        # La scelta dell'ottimo, sia personale, che globale è fallata.
        # Tra 2 soluzioni non dominate, anche se una migliore rispetto all'altra per più parametri la scelta è casuale.
        # Questo non porta a convergenza.
        # E' necessario creare i fronti di pareto.
        # Quindi il global Best viene scelto (casualmente?) nel primo fronte.
        # Per la scelta del personal best, si può procedere alla realizzazione di una repository 
        # di ottimi non dominanti tra loro, da tenere aggiornata (?)
        # Il global Best viene scelto creando lo sciame completo di tutte le soluzioni non dominanti incontrate.


        # [19,21,33]
        # [20,34,28] *
        # [25,33,34]  <- ALLA FINE QUESTA VINCE, ma e' DOMINATA...