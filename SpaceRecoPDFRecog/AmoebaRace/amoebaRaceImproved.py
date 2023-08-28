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

# class PriorityQueue:

#     pq = []


def makeEmpty():
    pq = []
    return pq

def find(pq, b):
    
    assert(b >= 0)
    n = len(pq)
    i = 0

    while i!= n:  # INV: i <= n and pq[i][1] != b
        if pq[i][1] == b: return i
        i = i + 1

    return i

def add(pq, a, b):
    
    n = len(pq)
    assert a >= 0 and b >= 0 and n <= N
    
    i = find(pq, b)

    if i == n:
        pq.append((a,b))
    
    else:
        
        if pq[i][0] > a:
            del pq[i]
            pq.append((a,b))
    

def getMin(pq):
    
    assert len(pq) <= N and len(pq) != 0

    minPq = pq[0] 
    assert(minPq[0] >= 0 and minPq[1]>= 0) # PRE: pq is non-empty and the time to reach the first destination is always postive.

    for x in pq[1:]: # Need to write the invariant for it here.
        if x[0] < minPq[0]:
            minPq = x
    
    pq.remove(minPq)
    return minPq

def isEmpty(amoebae):
    return len(amoebae) == 0

amoebae = makeEmpty()
add(amoebae, 0, 0)
# x = getMin(amoebae)

# print ("Min pq is-")
# print (x)
# print ("Amoeba is-")
# print(amoebae)
# print (isEmpty(amoebae))

while not isEmpty(amoebae):
    x,d= getMin(amoebae)
    print (x, d)
    board[d]= x
    print(board[d])
    print(graph1[d])
    for (l1,d1) in graph1[d]:
        print("case", (l1,d1))
        if board[d1]==-1: add(amoebae,x+l1,d1)
        print("amoeba here", amoebae)

print("in the improved ADT")
print(board)

    

