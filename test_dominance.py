import numpy as np

def pareto_dominance(array1, array2):
    if all(array1[i] <= array2[i] for i in range(len(array1))) and any(array1[j] < array2[j] for j in range(len(array1))):
        return True  # array1 domina array2
    elif all(array2[i] <= array1[i] for i in range(len(array1))) and any(array2[j] < array1[j] for j in range(len(array1))):
        return False  # array2 domina array1
    else:
        return None  # Nessuna dominanza

# Esempio di utilizzo
array1 = np.array([3, 9])
array2 = np.array([2, 8])

result = pareto_dominance(array1, array2)

if result is True:
    print("array1 domina array2")
elif result is False:
    print("array2 domina array1")
else:
    print("Nessuna dominanza tra array1 e array2")
