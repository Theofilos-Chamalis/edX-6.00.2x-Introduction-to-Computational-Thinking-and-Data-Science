# Enter code for the Cluster class in this box
class Cluster(object):
    """ A Cluster is defines as a set of elements, all having 
    a particular type """
    def __init__(self, points, pointType):
        """ Elements of a cluster are saved in self.points
        and the pointType is also saved """
        self.points = points
        self.pointType = pointType
    def singleLinkageDist(self, other):
        minDist = self.points[0].distance(other.points[0])
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) < minDist:
                    minDist = p1.distance(p2)
        return minDist
    def maxLinkageDist(self, other):
        maxDist = self.points[0].distance(other.points[0])
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) > maxDist:
                    maxDist = p1.distance(p2)
        return maxDist
    def averageLinkageDist(self, other):
        totDist = 0.0
        for p1 in self.points:
            for p2 in other.points:
                totDist += p1.distance(p2)
        return totDist/(len(self.points)*len(other.points))
    def members(self):
        for p in self.points:
            yield p
    def isIn(self, name):
        """ Returns True is the element named name is in the cluster
        and False otherwise """
        for p in self.points:
            if p.getName() == name:
                return True
        return False
    def toStr(self):
        result = ''
        for p in self.points:
            result = result + p.toStr() + ', '
        return result[:-2]
    def getNames(self):
        """ For consistency, returns a sorted list of all 
        elements in the cluster """
        names = []
        for p in self.points:
            names.append(p.getName())
        return sorted(names)
    def __str__(self):
        names = self.getNames()
        result = ''
        for p in names:
            result = result + p + ', '
        return result[:-2]
