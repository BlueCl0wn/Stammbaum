from person.Person import Person
from graph.Stammbaum import Stammbaum

test = Person(lastname="Lustig", firstname="Peter", middle_names=("Fritz"), gender="male",
              date_of_birth="2011-11-04T00:05:23", date_of_death="2015-11-04T00:05:23", place_of_birth="Hamburg",
              place_of_death="Berlin")

stamm = Stammbaum()



if __name__ == "__main__":
    print(test.lastname)
