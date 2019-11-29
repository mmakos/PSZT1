# GRAPH CLASS
# m_graph -> table of vertices, weights and costs
# vertex1 vertex2 weightBefore weightAfter cost   | with tabs between

class Graph:
    def __init__( self ):
        self.m_graph = []
        self.m_size = 0

    def addEdge( self, vertex1, vertex2, weightBefore = None, weightAfter = None, cost = None ):
        if vertex1 != vertex2:
            self.m_graph.append( sorted( [ vertex1, vertex2 ] ) + [ weightBefore, weightAfter, cost ] )  # adds sorted vertices to avoid duouble searching
            self.m_size += 1

    def saveToFile( self, fileName ):
        file = open( fileName, "wt" )
        for i in self.m_graph:
            file.write( f"{i[ 0 ] }\t{ i[ 1 ] }\t{ i[ 2 ] }\t{ i[ 3 ] }\t{ i[ 4 ] }\n")
        file.close()

    def loadFromFile( self, fileName ):
        file = open( fileName, "rt" )
        for line in file:
            line = line.split( "\t" )
            self.addEdge( line[ 0 ], line[ 1 ], int( line[ 2 ] ), int( line[ 3 ] ), int( line[ 4 ] ) )
        file.close()
        self.m_graph.sort()     # because we want to find edges in logn complexity

    def printGraph( self ):
        for i in self.m_graph:
            print( i )

    # Logarithmic - good
    # We can give 2 vertices in random order
    # returns edge index if it exists or -1 if it doesn't
    def getEdgeIndex( self, vertex1, vertex2 ):
        left = 1
        right = self.m_size
        edge = sotred( [ vertex1, vertex2 ] ) + [ 0, 0, 0 ]    # we don't care about anything except vertices so we can put 0
        while left < right:
            middle = ( left + right ) / 2
            if self.m_graph[ middle ] < y:
                left = middle + 1
            else:
                right = middle
        if self.m_graph[ left ] == edge:
            return left
        return -1   # there is no such edge

    # Returns edge (list) with given index
    def getEdge( self, index ):
        if number < m_size:
            return self.m_graph[ index ]

    # Linear - bad and unnecessary ( unless other doesn't work )
    #def getEdgeNumber( self, vertex1, vertex2 ):    
    #    for i in self.m_graph:
    #        if i[ :2 ] == sorted( [ vertex1 ][ vertex2 ] ):
    #            return i
    #    return -1

