import graph
import weights

g = graph.Graph()
w = weights.Weights()

g.loadFromFile( "graphTestMaxFlow" )
w.loadFromFile( "weightsTest" )
g.printGraph()

print( g.maxFlow( 1, 4 ) )


