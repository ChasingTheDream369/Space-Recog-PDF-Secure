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

# Get the line-width from the command line.
try:
    
    assert len(argv) == 2, "Expecting exactly one argument."
    
    M = int(argv[1])

    assert M >= 0, "Line width must be non-negative integer."

except: 
    
    assert False, "Usage: python3 %s WIDTH"%argv[0]
    
# Get the words from standard input into wds, and lengths into wls.
wds= []

for line in stdin.readlines(): 
    wds = wds+line.split()

wls = list(map(len,wds))
N = len(wds)

# Check that the input satisfies the program??s precondition.
for w in wls: assert w<=M

print("wds is",wds)
print("wls is",wls)
print("M is",M)
print("There are",N,"words in total.")