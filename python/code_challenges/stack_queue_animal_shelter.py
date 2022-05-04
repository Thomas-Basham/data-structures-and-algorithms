from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, animal):
        if animal.species == 'cat':
            self.cat.enqueue(animal)
        if animal.species == 'dog':
            self.dog.enqueue(animal)

    def dequeue(self, animal):
        if animal == 'cat':
            return self.cat.dequeue()
        if animal == 'dog':
            return self.dog.dequeue()
        else:
            return None


class Dog:
    def __init__(self):
        self.species = 'dog'


class Cat:
    def __init__(self):
        self.species = 'cat'

