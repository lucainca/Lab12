from model.model import Model

mymodel= Model()
mymodel.buildGraph("France",2015)
print(f" n nodi {mymodel.getNumNodes()} e n archi {mymodel.getNumEdges()}")