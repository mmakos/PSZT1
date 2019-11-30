import graph
import weights

g = graph.Graph()
w = weights.Weights()

g.loadFromFile( "graphTestMaxFlow" )
w.loadFromFile( "weightsTest" )
g.printGraph()

g.setWeights( w.getList(), [] )
print( g.maxFlow( False ) )


