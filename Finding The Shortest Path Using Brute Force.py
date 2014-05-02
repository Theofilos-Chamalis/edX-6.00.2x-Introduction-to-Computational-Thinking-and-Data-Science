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



def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.

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
    result = False
    paths = set()
    i = 0
    while result != None:
        i += 1
        result = mainRecursive([start], digraph, end, maxTotalDist, maxDistOutdoors)
        paths.add(tuple(result))
    return paths
    
def mainRecursive(path, digraph, end, maxTotalDist, maxDistOutdoors):
    global exploredNodes
    global exploredPaths
    global paths
    ##print path
    try:
        if path[-1] == end and tuple(str(path)) not in paths:
            ##print "This should only happen once per unique path."
            print "Path found: ", path,
            print "Total paths found:" + str(len(list(paths)))
            paths.add(tuple(str(path)))
            ##path = []
            exploredNodes = set([])
            ##return path
            if len(list(paths)) == 99:
                ##print "There are ", nodeChildren, "nodeChildren."
                allNodeChildren = digraph.childrenOf(path[-1])
                print "allNodeChildren =", allNodeChildren
                allNodeChildren = set(allNodeChildren)
                badChildren = exploredNodes.copy()
                nodeChildren = allNodeChildren - set(path)
                for i in nodeChildren:
                    if tuple(path + [i]) in exploredPaths:
                        badChildren.add(i)
                nodeChildren = nodeChildren - badChildren
                print "nodeChildren listed =", list(nodeChildren)[0]
                print "path =", path
                print sys.getrecursionlimit()
                return forward(list(nodeChildren)[0], path, digraph, end, maxTotalDist, maxDistOutdoors)
                ##print "There are", len(exploredNodes), "explored nodes."
                ##print "There are", len(exploredPaths), "explored paths."
    except:
        sys.exit("error")
    allNodeChildren = digraph.childrenOf(path[-1])
    allNodeChildren = set(allNodeChildren)
    badChildren = exploredNodes.copy()
    nodeChildren = allNodeChildren - set(path)
    for i in nodeChildren:
        if tuple(path + [i]) in exploredPaths:
            badChildren.add(i)
    nodeChildren = nodeChildren - badChildren
    if nodeChildren == set([]):
        return backward(path, digraph, end, maxTotalDist, maxDistOutdoors)
    else:
        ##print nodeChildren
        return forward(list(nodeChildren)[0], path, digraph, end, maxTotalDist, maxDistOutdoors)
    
def backward(path, digraph, end, maxTotalDist, maxDistOutdoors):
    global exploredPaths
    global exploredNodes
    global paths
    exploredNodes = set([])
    exploredPaths.add(tuple(path))
    path.pop()
    return mainRecursive(path, digraph, end, maxTotalDist, maxDistOutdoors)

def forward(node, path, digraph, end, maxTotalDist, maxDistOutdoors):
    global paths
    ##global exploredPaths
    global exploredNodes
    path.append(node)
    exploredNodes.add(node)
    return mainRecursive(path, digraph, end, maxTotalDist, maxDistOutdoors)