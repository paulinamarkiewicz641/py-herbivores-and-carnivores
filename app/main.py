class Animal:
    alive = []

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        # Custom string for each individual animal
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def __str__(cls):
        # Custom string for the Animal.alive list
        return str([repr(animal) for animal in cls.alive])

    def check_health(self):
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other):
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            if other.health < 0:
                other.health = 0
            other.check_health()


