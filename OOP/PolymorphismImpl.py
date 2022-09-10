class Dog():
    def __init__(self, name):
        self.name = name

    def do_sound(self):
        print("Wooof...")


class Cat():
    def __init__(self, name):
        self.name = name

    def do_sound(self):
        print("Meaw...")


philips = Dog("philips")
wello = Cat("wello")

philips.do_sound()
wello.do_sound()

# for pet in [philips, wello]:
#     print(type(pet))
#     print(type(pet.do_sound()))


def pet_speak(pet):
    print(pet.do_sound())


print("--------------")
pet_speak(philips)
pet_speak(wello)
