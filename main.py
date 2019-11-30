import graph
import weights
import graphGenerator

g = graph.Graph()
w = weights.Weights()

g.loadFromFile( "graph" )
w.loadFromFile( "weights" )
g.printGraph()

g.setWeights( w.getList(), [] )
print( g.maxFlow() )

print( "\n\n\n" )

gen = graphGenerator.Generator()

gen.generateGraphToFile( "generatedGraph", "generatedWeights" )


