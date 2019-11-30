import graph

g = graph.Graph()

g.loadFromFile( "graphTestMaxFlow" )
g.printGraph()

print( g.maxFlow( 1, 4 ) )


