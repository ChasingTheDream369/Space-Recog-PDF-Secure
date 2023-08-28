### COMP6721 2021T2 Assignment 1.
### NAME - SHUBHAM JOHAR.
### zid - z5284381.

### Paragraph.py --- Synopsis
#
# % python3 Paragraph.py WIDTH < WORDS
#
# The column WIDTH (non-negative integer) is given as the only argument;
# WORDS come from standard input, over as many lines as it takes, separated
# by white space. EOF from the terminal is ^D (as usual).
#
# The program prints WORDS in lines of exactly WIDTH characters, except
# possibly the last line, which might be shorter. It minimises the largest
# average white space between words in order to achieve the right-margin
# justification --- i.e. that the right margin is a straight vertical line.
#
# Although the average white space needed in a line might not be a
# whole number of blanks, the program simulates that in a fixed-width
# font by using a mixture of "just more than average" and "just less
# than average" inter-word gaps.

### Part (0) --- Collect input.
from sys import argv,stdin
from math import floor,ceil

# Get the line-width from the command line.
try:
    assert len(argv) == 2, "Expecting exactly one argument."
    M = int(argv[1])
    assert M >= 0, "Line width must be non-negative integer."

except: 
    assert False, "Usage: python3 %s WIDTH"%argv[0]
    
# Get the words from standard input into wds, and lengths into wls.
wds = []

for line in stdin.readlines(): 
    wds = wds + line.split()

wls = list(map(len,wds))
N = len(wds)

# Check that the input satisfies the program's precondition.
for w in wls: assert w<=M

print("wds is", wds)
print("wls is", wls)
print("M is", M)
print("There are", N, "words in total.")

### Part (1) --- Calculate minimum cost cs[n] for each suffix wds[n:].
### But wds is not needed in this part; use wls.

def Fits(l,h): # Whether wds[l:h] would fit within line-width M.

    assert (0 <= l < h <= N), "Fits() requires at least one word."
    numWords = sum(wls[l:h])
    numblanks = (M - sum(wls[l:h]))
    blanksNeeded = (h - l - 1)
    return (sum(wls[l:h]) <= M and numblanks>=blanksNeeded)  # (Boolean)

def Cost(l,h): # Average white-space length if wds[l:h] stretched to width M.

    assert Fits(l,h), "Cost() not meaningful if line doesn??t fit."
    blanksNeeded, words = (h-l-1), (h-l)
    blankSpaces = (M - sum(wls[l:h]))
    if (blanksNeeded != 0):
        avgCost = (blankSpaces)/(blanksNeeded)
    else:
        avgCost = blankSpaces
    
    return avgCost

# Precondition is that cs[n+1:] is already calculated.

def OverallCost(n,i): #Minimum cost of wds[n:] if first line is wds[n:i].
    
    assert (n<i), "OverallCost() line must not be empty."
    
    # Use INV1 below to help with this.
    assert Fits(n,i), "OverallCost() not meaningful if words don??t fit."
    return max(Cost(n, i), cs[i]) if i < N else 0

# The cost cs[n] will be the minimum averaged-per-line white space achievable
# for wds[n:] in line-width M, i.e. "from n on". (See INV1 below.)

cs, n = [0]*N, N # Pre-allocate cs; it will be filled from N-1 to 0.

while n!=0: # INV1(n) --- All of cs[n:] have correct values (as above).
    
    n, i = n-1, n # Only INV1(n+1) holds now.
    # print("The value of n is", n)
    # print("The value of i is", i)
    ci = OverallCost(n, i) #See INV2 below.
    # print("First ci", ci)

    # INV2(i) --- ci is the minimum...
    # ...of OverallCost(n,n+1), OverallCost(n,n+2), ..., OverallCost(n,i).

    while (i != N and Fits(n,i+1)): # Can one more word be added
        i = i+1
        # print("The value of i is", i)
        # Only INV2(i-1) holds now.
        ci = min(ci, OverallCost(n, i))
        # print("The value of ci is", ci)
        # INV2(i) is re-established.

    cs[n] = ci # INV1(n) is re-established.
    # print ("cs value is", cs)
# INV1(n) and n==0. Hence...
# INV1(0) and so cs is correct for the whole of wds.

print("cs is",cs)


# ### Part (2) --- Calculate actual optimal-cost paragraph,
# ### using wls and cs from Part (2).
# ### (This part does not use wds either.)

wlss, n = [],0

# INV3(n) --- # wls == flatten(wlss) + wls[n:]

while n != N:  # and for all ls in wlss: Cost(ls) <= cs[0]
              # and if n<N then cs[n] <= cs[0]

    i = n+1 # 1355: INV4 for this.
    
    #  1355: INV4(i) --- Fits(n,i).
    while OverallCost(n, i) > cs[n]: 
        i= i+1 # INV4 is maintained because the loop guard and the loop condition 
        # at each point intrisically calls the Fits for the new value of i and it continues uptil that 
        # condition holds and due to which invariant at each point of incrementing/ changing the variant holds in this
        # case.
    
    # OverallCost(n,i) <= cs[n]. # (This helps with KKK.)
    wlss= wlss+[wls[n:i]]
    n = i
    # INV3(n) re-established here.

print("wlss is",wlss)

## Part (3a) --- # Concatenate words in ls into a single line,
## separating them with b extra blanks in total,
## properly distributed.

def MakeLine(ls,b):
    
    assert b>=0, "1723: Extra blanks must not be negative."
    assert ls!=[], "1233: MakeLine(ls,b) requires ls!=[]."

    # If there's only one word, just put all blanks at the end.
    if len(ls)==1: return ls[0]+(" "*(M-len(ls[0])))

    # Otherwise, the usual case...
    # b is the number of blanks to distribute,
    # g is the number of inter-word gaps into which they must fit,
    # and each gap must receive between floor(b/g) and ceil(b/g) blanks.

    g= len(ls)-1
    b1,g1= b,g

    l= ls[0]
    # INV5(b1,g1): and b = b1 + "the number of avaialble spaces already mapped between the words"

    for w in ls[1:]:
        r = (b1/g1) if (b1%g1 == 0) else floor(b1/g1) # Number of blanks to put in this gap.
        
        assert floor(b/g)<=r<=ceil(b/g), "Space must not vary too much."
        l = l + ' '*(int(r)) + w 
        b1,g1= b1-r, g1 -1

    # b1==0 here, because all the available spaces have been mapped between words correctly
    # maintaining the invariant correctly.
    return l

## Part (3b) --- # Construct the lines of the paragraph,
##one-by-one, and print them out.

maxBlanks,lineCount= 0,0 # For reporting only.

for ws in wlss:
    ls,wds= wds[:len(ws)],wds[len(ws):] # Get the actual words.
    gapsHere= len(ws)-1

    if wds==[]: line= MakeLine(ls,gapsHere); print(line) # Last line.
    
    else:
        blanksNeededHere= M-sum(ws)
        line= MakeLine(ls,blanksNeededHere)
        maxBlanks= max(maxBlanks, \
        blanksNeededHere/gapsHere \
        if len(ws)>1 else blanksNeededHere)

        print("%s %d/%d = %.2f." % ( \
            line, blanksNeededHere, \
            gapsHere,blanksNeededHere/gapsHere \
            if len(ws)>1 else blanksNeededHere)
        )
    
    lineCount= lineCount+1

print(" "*M+"^")
print(("==> 567890"+("1234567890"*floor(M/10)))[:M]+"|")
print("==> The maximum (fractional) white space for column width" + \
" %3d was %.2f over %d lines." % \
(M, maxBlanks,lineCount))
