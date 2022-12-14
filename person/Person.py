import datetime
from dataclasses import dataclass


@dataclass
class Person:
    """
    Class describing a person with various variables.
    """

    lastname: str
    firstname: str
    nickname: str
    middle_names: tuple[str]
    birth_name: str

    gender: str

    date_of_birth: str
    date_of_death: str
    place_of_birth: str
    place_of_death: str

    parent1: type  # dad (if applicable)
    parent2: type  # mom (if applicable)
    biological_father: type
    biological_mother: type
    children: tuple[type] | type

    def __init__(self, lastname: str = None, firstname: str = None, nickname: str = None,
                 middle_names: tuple[str] = None,
                 birth_name: str = None, gender: str = None, date_of_birth: str = None, date_of_death: str = None,
                 place_of_birth: str = None, place_of_death: str = None, parent1: type = None, parent2: type = None,
                 biological_father: type = None, biological_mother: type = None, children: tuple[type] | type = None,
                 **kwargs):

        self.lastname = lastname
        self.firstname = firstname
        self.nickname = nickname
        self.middle_names = middle_names
        self.birth_name = birth_name

        self.gender = gender

        self.date_of_birth = date_of_birth
        self.date_of_death = date_of_death
        self.place_of_birth = place_of_birth
        self.place_of_death = place_of_death

        self.parent1 = parent1  # dad (if applicable)
        self.parent2 = parent2  # mom (if applicable)
        if parent1 == biological_father:
            self.biological_father = self.parent1
        if parent2 == biological_mother:
            self.biological_mother = self.parent2
        self.children = children

    def debug(self):
        pass

    def __hash__(self):
        return sum(map(hash, (self.firstname, self.middle_names, self.lastname, self.date_of_birth)))

    def __str__(self) -> str:
        name = (self.firstname, self.middle_names, self.lastname)
        temp = [i for i in name if i is not None]
        return " ".join(name)

    def add_relatives(self, **kwargs):
        self.__dict__.update(kwargs)

    def get_relatives(self) -> list:
        """
        Returns a list with all relationships of self in format [(self, Person, {"relation": "<relation>"}), ...].
        """
        relatives = (self.parent1, self.parent2, self.biological_father, self.biological_mother, self.children)
        return [(self, x) for x in relatives if x is not None]


if __name__ == "__main__":
    pass