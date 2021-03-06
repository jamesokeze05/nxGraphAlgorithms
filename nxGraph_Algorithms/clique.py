from functions.bool_functions import is_clique
from functions.global_properties import n, V
from itertools import combinations


def maximum_clique(G):
    for k in range (n(G), 1, -1):
        for S in combinations(V(G), k):
            if is_clique(G, list(S)) == True:
                return list(S)


def clique_numbers(G):
    return len(maximum_clique(G))
