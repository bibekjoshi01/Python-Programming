# Dynamic Polymorphism

"""Python follows Duck Typing, meaning "If it looks like a duck and quacks like a duck, it must be a duck."""


class Bird:
    def fly(self):
        return "I can fly, I am bird."


class Airplane:
    def fly(self):
        return "I am flying with jet engines!"


class Insect:
    def fly(self):
        return "I am insect, i can fly tooo."


def lets_fly(entity):
    """
    lets_fly() doesn’t check if entity is a Bird or Airplane.

    It only calls fly(), assuming the object has that method.
    """

    print(entity.fly())


lets_fly(Bird())
lets_fly(Airplane())
lets_fly(Insect())
