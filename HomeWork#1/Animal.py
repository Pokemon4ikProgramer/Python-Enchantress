class Animals:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def description_of_height(self):
        return self.name + "'s height is " + self.height


class Lion(Animals):
    def __init__(self, name, height):
        super().__init__(name, height)


class Giraffe(Animals):
    def __init__(self, name, height):
        super().__init__(name, height)


class Panda(Animals):
    def __init__(self,name, height):
        super().__init__(name, height)


class Lama(Animals):
    def __init__(self, name, height):
        super().__init__(name, height)


class Elephant(Animals):
    def __init__(self, name, height):
        super().__init__(name, height)


if __name__ == '__main__':
    animals = [Lion("Lion", "1.1m"),
               Giraffe("Giraffe", '5m'),
               Lama("lama", "1.7m"),
               Elephant("Elephant", "3m")]


