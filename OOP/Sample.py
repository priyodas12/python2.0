class Dog():
    def __init__(self, breed, age, cityOrigin, isMale):
        self.breed = breed
        self.age = age
        self.isMale = isMale
        self.cOrigin = cityOrigin
        # self.attribute_name is actual class property
        # arguments in init can difer


dog = Dog("pomerian", 14, "KOL", True)

print(dog.age, dog.breed, dog.cOrigin, dog.isMale)
