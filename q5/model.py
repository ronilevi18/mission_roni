

from typing import List
from .person import Person


class Model:
    def __init__(self):
        self.people: List[Person] = []

    def add(self, person: Person) -> None:
        self.people.append(person)

    def get_all(self) -> List[Person]:
        return list(self.people)
