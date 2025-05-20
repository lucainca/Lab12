import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._allCountries=[]
        self._allYears=[]
        self._allNodes=[]
        self._graph= nx.Graph()
        self._idMap={}
        for node in self._allNodes:
            self._idMap[node.Retailer_code] = node


    def buildGraph(self,country,year):

        self._allNodes = DAO.getNodes(country)

        self._graph.add_nodes_from(self._allNodes)


        for n1 in self._graph.nodes:
            for n2 in self._graph.nodes:
                if n1 != n2:
                    peso = DAO.getPeso(n1, n2, year)
                    if peso[0] > 0:
                        self._graph.add_edge(n1, n2, weight=peso[0])


    def getVolumeVendita(self):
        vicini= se



    def getAllCountries(self):

        self._allCountries = DAO.getCountries()
        return self._allCountries

    def getAllYears(self):
        self._allYears = DAO.getYears()
        return self._allYears

    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()
