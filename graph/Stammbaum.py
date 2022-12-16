import networkx as nx
from person.Person import Person


class Stammbaum(nx.DiGraph):
    persons: tuple

    def __init__(self, nodes, **attr):
        super().__init__(**attr)
        self.persons = nodes


        self.add_nodes_from(self.persons)
        self.add_relations(self.persons)

    def add_relations(self, person) -> None:
        """
        Adds relationships as edges to graph.

        :param graph:
        :param person:
        :return:
        """
        if person is Person:
            self.add_edges_from(person.get_relatives)
        if person is not Person:
            for i in person:
                self.add_edges_from(i.get_relatives())

    def write_graph(self, uri: str) -> None:
        """
        Saves graph as gml file at <uri>.

        :param graph:
        :param uri:
        :return:
        """
        nx.write_gml(self, uri)


if __name__ == "__main__":
    pass