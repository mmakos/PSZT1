import graph
import weights

g = graph.Graph()
w = weights.Weights()

g.loadFromFile( "generatedGraph" )
w.loadFromFile( "generatedWeights" )
# g.printGraph()

g.setWeights( w.getList(), [] )
print( g.maxFlow() )


