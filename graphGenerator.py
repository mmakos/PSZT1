import graph
import weights
import random

class Generator:
    def __init__( self ):
        self.g = graph.Graph()
        self.w = weights.Weights()

    def generateGraphToFile( self, graphFileName, weightsFileName, 
                            vertices = 50,  maxVertDiff = 10, edgeProb = 0.2, 
                            weightMin = 3, weightMax = 20, weightGrowMax = 5, costMin = 1, costMax = 5 ):
        random.seed()
        for i in range( vertices ):
            self.g._vertices.append( [ i, bool( random.randint( 0, 1 ) ) ] )
        for i in range( vertices ):
            for j in range( i + 1, min( i + maxVertDiff, vertices ) ):
                if random.random() < edgeProb:
                    self.g._addEdge( i, j )
        self.g.saveToFile( graphFileName )

        for i in range( self.g._size ):
            weightBefore = random.randint( weightMin, weightMax )
            self.w._list.append( [ weightBefore, weightBefore + random.randint( 1, weightGrowMax ), random.randint( costMin, costMax ) ] )
        self.w.saveToFile( weightsFileName )

