class Creature():
    def __init__(self):
        print("Creature CREATED!")

    def who_am_i(self):
        print("i am an Animal")


creature = Creature()
# print(animal)
creature.who_am_i()


class Cat(Creature):
    def __init__(self):
        Creature.__init__(self)
        print("CAT CREATED")

    def who_am_i(self):
        print("i am an Cat")


cat = Cat()
# print(cat)
print(cat.who_am_i())
