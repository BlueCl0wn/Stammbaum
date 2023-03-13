import networkx as nx
from person.Person import Person


class Stammbaum(nx.DiGraph):
    """
    Stellt einen Stammbaum dar. Dazu gehören Personen und Beziehungen innerhalb des Stammbaums
    """

    persons: tuple

    def __init__(self, nodes, **attr):
        super().__init__(**attr)
        self.persons = nodes

        self.add_nodes_from(self.persons)
        self.add_relations(self.persons)

    def add_relations(self, person: Person | list[Person] | tuple[Person]) -> None:
        """
        Adds relationships as edges to graph.

        :param graph:
        :param person: Object Person, list[Person] or tuple[Person]
        :return:
        """
        if type(person) == Person:
            self.add_edges_from(person.get_relatives)
        elif type(person) in (Person, list, list[Person], tuple[Person]):
            for i in person:
                self.add_edges_from(i.get_relatives())
        else:
            print(f"There was an error in Graph.add_relations(). Unsupported type. Requires either one of"
                  f"(Person, list, list[Person], tuple[Person]) not {type(person)}")

    def write_graph(self, uri: str) -> None:
        """
        Saves graph as gml file at <uri>.

        :param graph:
        :param uri:
        :return:
        :raise :
        """
        nx.write_gml(self, uri)


if __name__ == "__main__":
    pass
