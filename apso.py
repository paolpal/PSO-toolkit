from .myproblems import ConvToE
from .particle import PermutationParticle
from .pso import PSO

class APSO(PSO):
    def __init__(self, problem, num_particles, num_iterations, inertia_weight, c1, c2, **kwargs):
    #def __init__(self, num_iterations, inertia_weight, c1, c2, num_particles=None, num_dimensions=None, problem=None, **kwargs):
        #super().__init__(num_iterations, inertia_weight, c1, c2, **kwargs)
        self.num_iterations = num_iterations
        self.problem = problem

        self.num_particles = num_particles
        self.particles = [PermutationParticle(inertia_weight, c1, c2, problem.n_var, problem) for _ in range(num_particles)]
        
        self.global_best_position = self.get_global_best_position()

