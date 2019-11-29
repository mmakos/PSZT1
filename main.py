import graph

g = graph.Graph()

g.loadFromFile( "graphTest" )
g.printGraph()

print( g.getEdge( g.getEdgeIndex( '0', '4' ) ) )


