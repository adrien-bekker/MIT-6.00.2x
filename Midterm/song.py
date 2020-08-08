import random
  
# You are given this function - do not modify
def createRandomGraph():
    """Creates a digraph with 7 randomly chosen integer nodes from 0 to 9 and
    randomly chosen directed edges (between 10 and 20 edges)
    """
    g = {}
    n = random.sample([0,1,2,3,4,5,6,7,8,9], 7)
    for i in n:
        g[i] = []
    edges = random.randint(10,20)
    count = 0
    while count < edges:
        a = random.choice(n)
        b = random.choice(n)
        if b not in g[a] and a != b:
            g[a].append(b)
            count += 1
    return g

# You are given this function - do not modify
def findPath(g, start, end, path=[]):
    """ Uses DFS to find a path between a start and an end node in g.
    If no path is found, returns None. If a path is found, returns the
    list of nodes """
    path = path + [start]
    if start == end:
        return path
    if not start in g:
        return None
    for node in g[start]:
        if node not in path:
            newpath = findPath(g, node, end, path)
            if newpath: return newpath
    return None
                
#########################        
## WRITE THIS FUNCTION ##
#########################        

def allReachable(g, n):
    """
    Assumes g is a directed graph and n a node in g.
    Returns a sorted list (increasing by node number) containing all 
    nodes m such that there is a path from n to m in g. 
    Does not include the node itself.
    """
    reach = []
    for i in range(10):
        if n == i:
            continue
        else:
            if findPath(g, n, i):
                reach.append(i)
    
    return reach

def test():
    a = allReachable({0: [2], 1: [8, 3], 2: [4, 3, 8], 3: [4, 2, 0], 4: [8, 0], 5: [4, 1, 3], 8: [2, 0, 5, 3, 1]}, 8)
    print(a)

test()