import numpy as np
def make_graph(name):

        # make edges

        E= np.loadtxt(name, dtype='int')

        # make vertices

        v=[]

        for e in E:

            if e[0] not in v:

                v.append(e[0])

            if e[1] not in v:

                v.append(e[1])

        return (v,E)

G= make_graph('sample.txt')

print(G)