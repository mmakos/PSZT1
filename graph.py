class Graph:
    def __init__( self ):
        self.m_graph = []

    def addEdge( self, vertex1, vertex2, weight = None ):
        if vertex1 != vertex2:
            self.m_graph.append( sorted( [ vertex1, vertex2 ] ) + [ weight ] )  # adds sorted vertices to avoid duouble searching
            
    def setWeight( self, edgeNumber, weight ):
        self.m_graph[ edge ][ 2 ] = weight

    def getEdgeNumber( self, vertex1, vertex2 ):
        for i in self.m_graph:
            if i[ :2 ] == sorted( [ vertex1 ][ vertex2 ] ):
                return i
        return -1

    def saveToFile( self, fileName ):
        file = open( fileName, "wt" )
        for i in self.m_graph:
            file.write( f"{i[ 0 ] }\t{ i[ 1 ] }\t{ i[ 2 ] }\n")
        file.close()

    def loadFromFile( self, fileName ):
        file = open( fileName, "rt" )
        for line in file:
            line = line.split( "\t" )
            self.addEdge( line[ 0 ], line[ 1 ], int( line[ 2 ] ) )
        file.close()

    def printGraph( self ):
        for i in self.m_graph:
            print( i )
