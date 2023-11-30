import numpy as np
from problem import Problem
from particle import Particle
from  pso import PSO
import copy
import random

class MOPSO(PSO):
    def __init__(self, problem, num_particles, num_iterations, inertia_weight, c1, c2, preferred_obj=None, **kwargs):
        self.num_iterations = num_iterations
        self.problem = problem
        # Inizializza le particelle
        self.num_particles = num_particles
        self.particles = [Particle(inertia_weight, c1, c2, problem.n_var , problem) for _ in range(num_particles)]
            
        # Inizializza la miglior posizione globale
        self.preferred_obj = preferred_obj if preferred_obj else None
        
        self.global_best_position = self.get_global_best_position()

    def dominate(self, x_obj, y_obj):
        dom=True
        for i in range(self.problem.n_obj):
            less = x_obj[i] <= y_obj[i]
            dom &= less
        return dom
    
    def better(self, x_obj, y_obj):
        if self.preferred_obj:
            return x_obj[self.preferred_obj] < y_obj[self.preferred_obj]
        else:
            return random.choice([True, False])
    
    def get_global_best_position(self):
        global_best_position = self.particles[0].best_position
        global_best_fitness = self.problem.evaluate(self.particles[0].best_position)
        for particle in self.particles[1:]:
            particle_best_fitness = self.problem.evaluate(particle.best_position)
            if self.dominate(particle_best_fitness, global_best_fitness):
                global_best_position = copy.deepcopy(particle.best_position)
            elif not self.dominate(global_best_fitness, particle_best_fitness):
                if self.better(particle_best_fitness, global_best_fitness):
                    global_best_position = copy.deepcopy(particle.best_position)
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
            particle_best_fitness = self.problem.evaluate(particle.best_position)
            if self.dominate(particle.fitness, particle_best_fitness):
                particle.best_position = np.copy(particle.position)
            elif not self.dominate(particle_best_fitness, particle_best_fitness):
                if self.closer_to_origin(particle.fitness, particle_best_fitness):
                    particle.best_position = copy.deepcopy(particle.position)

        self.global_best_position = self.get_global_best_position()        