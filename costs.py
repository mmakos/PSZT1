class Costs:
    def __init__( self ):
        self.m_costs = []

    def loadCostsFromFile( self, fileName ):
        file = open( fileName, "rt" )
        self.m_costs = file.read().split( " " )

    def printCosts( self ):
        print( self.m_costs )
