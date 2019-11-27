import graph
import costs

g = graph.Graph()
c = costs.Costs()

g.loadFromFile( "graphTest" )
g.printGraph()
c.loadCostsFromFile( "costsTest" )
c.printCosts()


