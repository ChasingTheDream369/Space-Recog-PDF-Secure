### Simulation of Reynold's "amoeba race" shortest-path algorithm.

from sys import stdin # For readlines().

# Enter graph from stdin, one edge per line; finish with ^D (if on terminal).
print("Enter source length destination , one triple per line for each edge:")
graph= [tuple(map(int,line.split())) for line in stdin.readlines()]

# Validate input.
assert graph!=[], "Graph must not be empty."

for (s,l,d) in graph:
    assert s>=0 and d>=0 and l>0, \
    "Node number must be non-negative, and distances positive."
print(graph)

# How many nodes?
n= 0
for (s,l,d) in graph:
    n= max(n,s,d)
N= n+1 # Node numbers are 0:N, but some nodes might be isolated.

board= [-1]*N # Blank board is -1.
t= 0 # Clock starts at 0.

# Amoebae positions are (sourceNode, distanceFromDestination, destinationNode).
amoebae= [(0,0,0)] # The ur-amoeba is now at Node 0.

print ("Variant finding")
while amoebae!=[]: # While at least one amoeba still lives.

    movingAmoebae= []
    print("amobae lengths is ")
    for a in amoebae:
        print (a[1])

    print('\n')

    for a in amoebae:
        s,l,d= a # source,length,destination
        if l==0: # Just arrived at Node d.
            
            if board[d]==-1:
                board[d]= t
                for e in graph: #1031: Check for outgoing edges.
                    if e[0]==d: 
                        movingAmoebae.append(e)

        else: # Between nodes.
            movingAmoebae.append(a)

    # Clock ticks; the amoebae move.
    amoebae= [(s,l-1,d) for (s,l,d) in movingAmoebae]
    t= t+1


print(board)