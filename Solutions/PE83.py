# Project Euler 83

def str2int(l):
    L = []
    for element in l:
        L.append(int(element))
    return L

data = []
with open("matrix.txt") as f:
    for line in f.readlines():
        data.append(str2int(line.split(",")))

class Queue(object):

    
    def __init__(self):
        self.l = []
        
    def add(self, node):
        self.l.append(node)

    def isEmpty(self):
        return len(self.l) == 0

    def getSmallest(self, dist):
        smallest = dist[self.l[0]]
        smallestNode = self.l[0]
        for node in self.l:
            result = dist[node]
            if result < smallest:
                smallest = result
                smallestNode = node
        return smallestNode

    def remove(self, node):
        self.l.remove(node)

def getNeighbors(node):
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    result = []
    row, col = node[0], node[1]
    for dir in dirs:
        if 0 <= row+dir[0] < 80 and 0 <= col+dir[1] < 80:
            # within the range
            result.append((row+dir[0],col+dir[1]))
    return result

def distance(u,v, dist):
    return data[v[0]][v[1]]
    
def dijkstra(graph=data, source=(0,0)):
    rows, cols = len(graph), len(graph[0])
    dist = dict()
    for row in xrange(rows):
        for col in xrange(cols):
            dist[(row,col)] = float("inf")
    dist[source] = data[0][0]

    Q = Queue()
    for row in xrange(rows):
        for col in xrange(cols):
            Q.add((row,col))

    while Q.isEmpty() == False:
        u = Q.getSmallest(dist)
        Q.remove(u)
        # if dist[u] == float("inf"):
            # break
        for v in getNeighbors(u):
            alt = dist[u] + distance(u, v, dist)
            if alt < dist[v]:
                dist[v] = alt
        
    print dist[(79,79)]

dijkstra()    

               
