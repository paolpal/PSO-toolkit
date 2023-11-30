from myproblems import Schaffer1
from mopso import MOPSO
import matplotlib.pyplot as plt

n_particles = 40
n_iterations = 400
c1 = .75  # Coefficiente cognitivo
c2 = 1.5  # Coefficiente sociale
w = .5   # Inerzia
preferred_objective_index = 0  # Indice dell'obiettivo preferito

my_mo_problem = Schaffer1()

mopso = MOPSO(my_mo_problem, n_particles, n_iterations, w, c1, c2)

pos, fit = mopso.run()
print(f"{pos} , {fit}")

for particle in mopso.particles:
    pass
    #print(f"{particle.position} , {particle.fitness}")

x = [particle.fitness[0] for particle in mopso.particles]
y = [particle.fitness[1] for particle in mopso.particles]

plt.scatter(x, y)
 
# To show the plot
plt.show()