### Simulation of Reynold's "amoeba race" shortest-path algorithm.
from sys import stdin # For readlines().

# Enter graph from stdin, one edge per line; finish with ^D (if on terminal).
print("Enter source length destination , one triple per line for each edge:")
graph= [tuple(map(int,line.split())) for line in stdin.readlines()]


# Validate input.
assert graph!=[], "Graph must not be empty."
for (s,l,d) in graph:
    assert s>=0 and d>=0 and l>0, "Node number must be non-negative, and distances positive."

print(graph)

# How many nodes?
n= 0

# Taking into consideration that 
for (s,l,d) in graph:
    n= max(n,s,d)



N= n+1 # Node numbers are 0:N, but some nodes might be isolated
#(as in some nodes will not be having any edges because we have not
# defined their edge relationships/ distance between the node edges 
# but they will still exists as isolated edges in the world).
# We add one to the number n that we have found which is the maximum 
# edge number we have inputted to have the relationship of it with the 
# other node numbers as well, but in reality what we have here is that total
# nodes that we will conisder for the amoeba to move will be max node number + 1,
# where some of the nodes are still isolated and might not be 
# vey relevant completely, so we might need to map it in completely. 

print (N)


graph1 = [[] for i in range(N)]

for g in graph:
    graph1[g[0]].append(g[1:])
    
print (graph1)

board= [-1]*N # Blank board is -1.
t= 0 # Clock starts at 0.

# Amoebae positions are (sourceNode, distanceFromDestination, destinationNode).
amoebae= [(0,0)] # The ur-amoeba is now at Node 0.

while amoebae!=[]: # While at least one amoeba still lives.

    movingAmoebae= []
    
    for a in amoebae:
        
        l,d= a # source,length,destination
        if l==0: # Just arrived at Node d.
            if board[d]==-1:
                board[d]= t
                print("Arrived at Node %d at Time %d."%(d,t))
                print("amoebae's active", amoebae)
            # for e in graph:
            #     if e[0] == d: movingAmoebae.append(e[1:])
            # # if  board[e[2]] == -1: 
                for g in graph1[d]:
                    if (board[g[1]] == -1): movingAmoebae.append(g)

        else: # Between nodes.
            movingAmoebae.append(a)

    # Clock ticks; the amoebae move.
    amoebae= [(l-1,d) for (l,d) in movingAmoebae]
    print(f"Board at the time instant {t} is")
    print(board)
    t= t+1
    

print("Final board is")
# print("\n")
# print("\n")
print(board)