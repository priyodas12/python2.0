class Dog():
    def __init__(self, breed, age, cityOrigin):
        self.breed = breed
        self.age = age
        self.cOrigin = cityOrigin
        # self.attribute_name is actual class property
        # arguments in init can difer


dog = Dog("pomerian", 12, "BLR")

print(dog.age, dog.breed, dog.cOrigin)
