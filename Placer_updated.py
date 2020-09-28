G,N = list(map(int,input().split(" ")))
gates = []
degree = []
edges = []
for i in range(G):
    x= list(map(int,input().split(" ")))
    gates.append(x[0])
    degree.append(x[1])
    edges.append(x[2:])
#print(gates)
#print(degree)
#print(edges)
inverse_gate_wire = [[0 for i in range(G)] for j in range(N)]
gate_wire= [[0 for i in range(N)] for j in range(G)] #gate as rows and wire as columns
for i in range(len(edges)):
    for j in range(len(edges[i])):
        x=edges[i][j]
        gate_wire[i][x-1]=1
        inverse_gate_wire[x-1][i]=1
#print("-------------gate_wire-------------------")        
#print(gate_wire)
#print( "                                          ")

gate_gate=[[0 for i in range(G)] for j in range(G)] #which gate in row is connected to which gate in column
for i in range(len(gate_wire)):
    for j in range(len(gate_wire[i])):
        for c in range(len(gate_wire)-i-1):
            if (gate_wire[i][j]==gate_wire[i+1+c][j]) & (gate_wire[i][j]!=0):
                gate_gate[i][i+1+c]=1
                gate_gate[i+1+c][i]=1
#print("--------------gate_gate-----------------")
#print(gate_gate)
#print("                                        ")

k_point_breaking = []
for i in range(len(inverse_gate_wire)):    
    if (sum(inverse_gate_wire[i])>2):
        k_point_breaking.append(inverse_gate_wire[i])
#print("-------------------k_point_breaking----------------------")                
#print(k_point_breaking)
#print("                                        ") #store the gates which are connected as k point
k_updated = []
for i in range(len(k_point_breaking)):
    k_k = []
    for j in range(len(k_point_breaking[i])):
        if (k_point_breaking[i][j]==1):
            k_k.append(j)
    k_updated.append(k_k)
print("k_updated = " ,k_updated)
print(gate_gate)
print(len(k_updated))
l=0
for i in range(len(k_updated)):
    for j in range(len(k_updated[i])):
        for m in range(len(k_updated[i])):
            kk=len(k_updated[0])
            k=1/(kk-1)
            x=k_updated[i][j]
            y=k_updated[i][m]
            gate_gate[x][y]*=k    

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
    nl.append(gate_wire[i])
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
            if (gate_wire[i][k]==newlist[j][k]) and (gate_wire[i][k]!=0):
                gate_pads[i][j] = 1               
            
x = gate_gate[:]
for i in range(len(gate_gate)):
    for j in range(len(gate_gate[i])):
        gate_gate[i][j]=(gate_gate[i][j])*(-1)

for i in range(len(gate_pads)):
    if (sum(gate_pads[i])==1):
        gate_gate[i][i]=(sum(x[i])*(-1))+1
    else:
        gate_gate[i][i]=(sum(x[i])*(-1))
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
xc=solve(gate_gate,Bx)
yc=solve(gate_gate,By)


import matplotlib.pyplot as plt
#plt.xlim(0,100)
#plt.ylim(0,100)
plt.plot(xc,yc,"^")
plt.show()






        
