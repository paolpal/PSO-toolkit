from random import choice, shuffle
import numpy as np
import math

def compose_permutations(p1, p2):
    """Composizione di due permutazioni."""
    return [p1[p2[i] - 1] for i in range(len(p1))]

def inverse_permutation(p):
    """Calcola l'inverso di una permutazione."""
    if isinstance(p, np.ndarray):
        p=p.tolist()
    return [p.index(i + 1) + 1 for i in range(len(p))]

def swap_values(array, index):
    array_copy = array.copy()
    array_copy[index], array_copy[index + 1] = array_copy[index + 1], array_copy[index]
    return array_copy

def update_A(A, All, i, p):
    n = len(p)-1
    if i > 0 and All[i-1] not in A and p[i-1] > p[i]:
        A.append(All[i-1])
    if i < n-1 and All[i+1] not in A and p[i+1] > p[i+2]:
        A.append(All[i+1])
    return A

def add(p1, p2):
    return compose_permutations(p1, p2)

def sub(p1, p2):
    return compose_permutations(inverse_permutation(p2), p1)

def randbs_decomposition(p):
    """Algoritmo RandBS per la decomposizione casuale di una permutazione."""
    s = []
    perm_sorted = list(range(1, len(p)+1))
    moves = ([swap_values(perm_sorted, i) for i in range(len(p) - 1)])
    All = [swap_values(perm_sorted, i) for i in range(len(p) - 1)]
    All = list(enumerate(All))
    A = [(i,a) for i,a in All if p[i] > p[i + 1] ]
    while A:
        i, move = choice(A)
        p = compose_permutations(p, move)
        s.append(move)
        A.remove((i, move))
        A = update_A(A, All, i, p)

    s.reverse()
    return s

def truncate(a, p):
    s = randbs_decomposition(p)
    l = len(s)
    k = math.ceil(a*l)
    z = list(range(1, len(p)+1))
    for i in range(1, k):
        z = add(z,s[i])
    return z

def extend(a, p):
    w = list(range(1, len(p)+1))
    w.reverse()
    D = len(randbs_decomposition(w)) 
    s = randbs_decomposition(sub(w,p))
    l = D - len(s)
    a_x = D/l if l != 0 else float('inf')
    a = min(a, a_x)
    k = math.ceil(a*l)
    z = p
    for i in range(1,k-l):
        z = add(z, s[i])
    return z

def mul(a, p):
    if(a<=1):
        res = truncate(a, p)
    else:
        res = extend(a, p)

    return res

# Esempio di utilizzo
if __name__ == "__main__":
    p1 = [3, 1, 2, 4, 5, 6]
    p2 = [1, 2, 3, 5, 6, 4]
    p3 = [10, 5, 7, 4, 8, 6, 3, 9, 2, 1]#np.random.permutation(10)+1

    e = [1,2,3,4,5]
    w = [5,4,3,2,1]
    p5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # Composizione di permutazioni
    result_compose = compose_permutations(p1, p2)
    print("Composizione di permutazioni:", result_compose)

    # Calcolo dell'inverso di una permutazione
    result_inverse = inverse_permutation(p1)
    print("Inverso di una permutazione:", result_inverse)

    # RandBS decomposition
    result_randbs = randbs_decomposition(p1)
    print("Decomposizione RandBS len:", len(result_randbs))

    a = add(p1,p2)
    print("Somma:", a)

    a = sub(p1,p2)
    print("Differenza:", a)

    a = mul(0.5, e)
    print("Moltiplicazione:", a)


