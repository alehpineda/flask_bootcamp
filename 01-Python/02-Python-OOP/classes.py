class Dog():
    # class object
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

sam = Dog('Huskie', 'Sammy')
new_dog = Dog('Golden', 'Cindy')

print(sam.breed, sam.breed, sam.species)
print(new_dog.breed, new_dog.name, new_dog.species)

class Circle():
    pi = 3.141692

    def __init__(self, radius=1):
        self.radius = radius
    
    
    def area(self):
        return self.radius * self.radius * self.pi
    

    def circumference(self):
        return 2 * self.radius * self.pi
    

myCircle = Circle(10)

print(myCircle.area(), myCircle.circumference())


