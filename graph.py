# GRAPH CLASS
# m_graph -> table of vertices, weights and costs
# m_size -> quantity of edges
# m_vertices -> list of vertices, needed for bfs algorithm and if they are or they are not cities
# vertex1 vertex2 weight   | with tabs between

class Graph:
    def __init__( self ):
        self.m_graph = []
        self.m_size = 0
        self.m_vertices = []

    def addEdge( self, vertex1, vertex2, weight = None ):
        if vertex1 != vertex2:
            self.m_graph.append( sorted( [ vertex1, vertex2 ] ) + [ weight ] )  # adds sorted vertices to avoid duouble searching
            self.m_size += 1

    def saveToFile( self, fileName ):
        file = open( fileName, "wt" )
        for i in self.m_graph:
            file.write( f"{i[ 0 ] }\t{ i[ 1 ] }\t{ i[ 2 ] }\n")
        file.close()

    def loadFromFile( self, fileName ):
        file = open( fileName, "rt" )
        vertices = file.readline().split()
        isCity = file.readline().split()
        self.m_vertices = [ ( int( vertices[ i ] ), int( isCity[ i ] ) ) for i in range( 0, len( vertices ) ) ]
        for line in file:
            line = line.split( "\t" )
            self.addEdge( int( line[ 0 ] ), int( line[ 1 ] ) )
        file.close()
        self.m_graph.sort()     # because we want to find edges in logn complexity

    def printGraph( self ):
        print( self.m_vertices )
        for i in self.m_graph:
            print( i )

    # Logarithmic - good
    # We can give 2 vertices in random order, vertices must be strings
    # returns edge index if it exists or -1 if it doesn't
    def getEdgeIndex( self, vertex1, vertex2 ):
        left = 1
        right = self.m_size
        edge = sorted( [ vertex1, vertex2 ] ) + [ None ]    # we don't care about anything except vertices so we can put 0
        while left < right:
            middle = int( ( left + right ) / 2 )
            if self.m_graph[ middle ] < edge:
                left = middle + 1
            else:
                right = middle
        if self.m_graph[ left ][ :2 ] == edge[ :2 ]:
            return left
        return -1   # there is no such edge

    # Returns edge (list) with given index
    def getEdge( self, index ):
        if index < self.m_size:
            return self.m_graph[ index ]

    
    # Edmonds-Karp algorithm ( extended Ford-Fulkerson method )
    # Finds maximum flow in a flow network
    def maxFlow( self, begin, end ):
        ############## ancillary variables
        Q = []      # queue of vertices to visit
        P = []      # list of visited neighbors
        F = []      # list of used flows
        CFP = []    # list of residual capacity for path ending in some node of network ( we want to take minimum )
        cp = abs    # residual capacity = total capacity - flow used
        fmax = 0    # maximal flow - that is what we are looking for
        escape = True
        for i in range( 0, m_size ):
            F[ i ] = 0

        while escape:
            ############## variables initialization
            for i in range( 0, len( self.m_vertices ) ):
                P[ i ] = -1
            CPF[ begin ] = int( 'ffffffff', 16 )
            P[ begin ] = -2
            Q.clear()
            Q.append( begin )
            ############## actual begin of algorithm                                           # add begin vertex to queue of vertices to visit
            while Q:
                escape = False                                          # to end algorithm when it's time
                x = Q.pop( 0 )                                          # take first vertex from queue
                for y in range( 0, len( self.m_vertices ) ):            # look for all vertices not visited and having connection with x
                    index = self.getEdgeIndex( x, y )                   # look for edge ( x, y ) or ( y, x )
                    cp = self.m_graph[ index ][ 2 ] - F[ index ]        # count residual capacity
                    if index != -1 and P[ y ] == -1 and cp != 0:        # if edge exists and if neighbor of x - y was not examined yet and cp is not 0
                        P[ y ] = x                                      # remember previous on path
                        CFP[ y ] = min( CFP[ x ], cp )                  # cout residual capacity to y vertex
                        if y == end:                                    # if reached end
                            escape = True                               # end bfs algorithm but don't end whole algorithm because we found next path                          
                            break
                        Q.append( y )                                   # add y to vertices to visit
                if escape:                                              # if bfs should be ended
                    break                                               # end it
            fmax += CFP[ end ]                                          # add residual capacity to maximum flow
            y = end
            while y != begin:                                           # go back along the path from end to begin
                F[ self.getEdgeIndex( P[ y ], y ) ] += CFP[ end ]       # add to used flow recently counted residual capacity
                y = P[ y ]                                              # go to previous vertex of the path
            if not escape:                                              # if didn't find path
                break                                                   # end algorithm
        return fmax                                                     # and return fmax