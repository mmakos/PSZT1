# WEIGHTS CLASS
# Stores list of weights and costs
# weightBefore, weightAfter, cost

class Weights:
    def __init__( self ):
        self._list = []

    def loadFromFile( self, fileName ):
        file = open( fileName, "rt" )
        for line in file:
            line = line.split( "\t" )
            self._list.append( [ int( line[ 0 ] ), int( line[ 1 ] ), int( line[ 2 ] ) ] )
