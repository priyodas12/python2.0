class Dog():
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age


dog = Dog("pomerian", 12)

print(dog.age, dog.breed)
