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