from person.Person import Person
from graph.Stammbaum import Stammbaum

a = Person(lastname="Petersen", firstname="Monika", gender="female")
b = Person(lastname="Petersen", firstname="Herrmann", gender="male")
c = Person(lastname="Petersen", firstname="Käthe", gender="male")
a.add_relatives(parent1=b, parent2=c)
b.add_relatives(children=a)
c.add_relatives(children=a)
print(str(a))
#a.debug()
persons = [a, b, c]

B = Stammbaum(persons)
B.nodes()
B.edges()
