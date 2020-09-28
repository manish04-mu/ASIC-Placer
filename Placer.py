G,N = list(map(int,input().split(" ")))
gates = []
degree = []
edges = []
for i in range(G):
    x= list(map(int,input().split(" ")))
    gates.append(x[0])
    degree.append(x[1])
    edges.append(x[2:])

l= [[0 for i in range(N)] for j in range(G)]
for i in range(len(edges)):
    for j in range(len(edges[i])):
        x=edges[i][j]
        l[i][x-1]=1

ac=[[0 for i in range(G)] for j in range(G)]
for i in range(len(l)):
    for j in range(len(l[i])):
        for c in range(len(l)-i-1):
            if (l[i][j]==l[i+1+c][j]) & (l[i][j]!=0):
                ac[i][i+1+c]=1
                ac[i+1+c][i]=1


P =  int(input ())
pads = []
pads_edges = []
pads_coordinates = []
for i in range(P):
    x = list(map(int,input().split()))
    pads.append(x[0])
    pads_edges.append(x[1])
    pads_coordinates.append(x[2:])

nl = []
for i in range(G):
    nl.append(l[i])
for i in range(P):
    nl.append([0 for i in range(N)])
for i in range(len(pads_edges)):
    x=pads_edges[i]
    nl[G+i][x-1]=1


newlist = []
for i in range (G,G+P):
    newlist.append(nl[i])

gate_pads = [[0 for i in range(P)] for j in range(G)]

for i in range(G):
    for j in range(P):
        for k in range(N):
            if (l[i][k]==newlist[j][k]) and (l[i][k]!=0):
                gate_pads[i][j] = 1               
            
x = ac[:]
for i in range(len(ac)):
    for j in range(len(ac[i])):
        ac[i][j]=(ac[i][j])*(-1)

for i in range(len(gate_pads)):
    if (sum(gate_pads[i])==1):
        ac[i][i]=(sum(x[i])*(-1))+1
    else:
        ac[i][i]=(sum(x[i])*(-1))
Bx =[0 for i in range(G)]
for i in range(G):
    for j in range(P):
        if gate_pads[i][j]==1:
            Bx[i] = pads_coordinates[j][0]
            
            
            
By =[0 for i in range(G)]
for i in range(G):
    for j in range(P):
        if gate_pads[i][j]==1:
            By[i] = pads_coordinates[j][1]
                 

import numpy as np
from scipy.linalg import solve
xc=solve(ac,Bx)
yc=solve(ac,By)


import matplotlib.pyplot as plt
#plt.xlim(0,1)
#plt.ylim(0,1)
plt.plot(xc,yc,"o")
plt.show()
print(l)
print(ac)