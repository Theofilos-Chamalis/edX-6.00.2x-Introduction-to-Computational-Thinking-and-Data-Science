class WeightedDigraph(Digraph):
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append((dest, edge.getTotalDistance(), edge.getOutdoorDistance()))
   
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res += '{0}->{1} ({2}, {3})\n'.format(k, d[0], float(d[1]), float(d[2]))
        return res
       
    def childrenOf(self, node):
        res = []
        for e in self.edges[node]:
            res.append(e[0])
        return res        
   
class WeightedEdge(Edge):
    def __init__(self, src, dest, dist, out_dist):
        self.src = src
        self.dest = dest
        self.dist = dist
        self.out_dist = out_dist
       
    def getTotalDistance(self):
        return self.dist
       
    def getOutdoorDistance(self):
        return self.out_dist
       
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.dist, self.out_dist)


def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
   Finds the shortest path from start to end using directed depth-first.
   search approach. The total distance travelled on the path must not
   exceed maxTotalDist, and the distance spent outdoor on this path must
        not exceed maxDisOutdoors.
 
   Parameters:
       digraph: instance of class Digraph or its subclass
       start, end: start & end building numbers (strings)
       maxTotalDist : maximum total distance on a path (integer)
       maxDistOutdoors: maximum distance spent outdoors on a path (integer)
 
   Assumes:
       start and end are numbers for existing buildings in graph
 
   Returns:
       The shortest-path from start to end, represented by
       a list of building numbers (in strings), [n_1, n_2, ..., n_k],
       where there exists an edge from n_i to n_(i+1) in digraph,
       for all 1 <= i < k.
 
       If there exists no path that satisfies maxTotalDist and
       maxDistOutdoors constraints, then raises a ValueError.
   """
    def getPathDistance(path):
        distance, outDistance = 0, 0
        if path == None:
            return maxTotalDist, maxDistOutdoors
        for i in range(len(path)-1):
            src, dest = path[i], path[i+1]
            distance += digraph.getEdgeTotalWeight(src, dest)
            outDistance += digraph.getEdgeOutWeight(src, dest)
        return distance, outDistance
 
    def DFS(start, end, path=[], shortest=None, currentDistance=0, currentOutDistance=0):
        path = path + [start]
        maxDistance, maxOutDistance = getPathDistance(shortest)
        if start == end:
            return path
        for node in digraph.childrenOf(start):
            if node not in path:
                currentDistance += digraph.getEdgeTotalWeight(start, node)
                currentOutDistance += digraph.getEdgeOutWeight(start, node)
                if currentDistance <= maxDistance and currentOutDistance <= maxOutDistance:
                    newPath = DFS(node, end, path, shortest, currentDistance, currentOutDistance)
                    if newPath != None:
                        shortest = newPath
        return shortest
 
    result = DFS(start, end)
    return result