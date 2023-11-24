import numpy as np
from problem import Problem
import algebric
import random

class Particle:
    def __init__(self, inertia_weight, c1, c2, num_dimensions=None,problem=None):
        if num_dimensions:
            self.num_dimensions = num_dimensions
            self.position = np.random.rand(num_dimensions)
            self.velocity = np.random.rand(num_dimensions)
            self.best_position = np.copy(self.position)
        if problem:
            self.fitness = problem.evaluate(self.position)
        self.inertia_weight = inertia_weight
        self.c1 = c1
        self.c2 = c2

    def evaluate_fitness(self, problem):
        self.fitness = problem.evaluate(self.position)

    def update_velocity(self, global_best_position):
        # Aggiorna la velocità della particella
        inertia_term = self.inertia_weight * self.velocity
        r1 = np.random.rand()
        r2 = np.random.rand()
        cognitive_term = self.c1 * r1 * (self.best_position - self.position)
        social_term = self.c2 * r2 * (global_best_position - self.position)

        self.velocity = inertia_term + cognitive_term + social_term

    def update_position(self):
        # Aggiorna la posizione della particella
        self.position = self.position + self.velocity

class PermutationParticle(Particle):
    def __init__(self, inertia_weight, c1, c2, num_dimensions, problem):
        super().__init__(inertia_weight, c1, c2)
        self.position = np.random.permutation(num_dimensions)+1
        self.velocity = np.random.permutation(num_dimensions)+1
        self.best_position = np.copy(self.position)
        self.fitness = problem.evaluate(self.position)


    def update_velocity(self, global_best_position):
        # Aggiorna la velocità della particella
        inertia_term = algebric.mul(self.inertia_weight,self.velocity)
        r1 = np.random.rand()
        r2 = np.random.rand()
        #print(self.position)
        cognitive_term = algebric.mul(self.c1 * r1 , algebric.sub(self.best_position, self.position))
        social_term = algebric.mul(self.c2 * r2 , algebric.sub(global_best_position, self.position))

        permutations = [inertia_term, cognitive_term, social_term]

        # Mescola l'ordine delle permutazioni
        random.shuffle(permutations)

        # Somma delle permutazioni nell'ordine casuale
        self.velocity = permutations[0]
        for perm in permutations[1:]:
            self.velocity = algebric.add(self.velocity, perm)

    def update_position(self):
        # Aggiorna la posizione della particella
        self.position = algebric.add(self.position, self.velocity)
