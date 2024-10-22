class Animal:
    def __init__(self,name,age):
        self.name=name
        #self.__age=age  (Private property)
        self.age=age
    def get_age(self):
        return f"{self.name} is {self.age} years old."
    def __str__(self): #Return meaningful output when someone prints a object
        return f"{self.name} is {self.age} years old."
class Dog(Animal):
    species="canis familiaries"
    def bark(self):
        return f"{self.name} says woof!"
    
    
class Cat(Animal):
    species="cat species"
    def mew(self):
        return f"{self.name} says meow!"

print("Dog class")
dog1=Dog("Buddy",3)
dog2=Dog("Charlie",5)
print(dog1.bark())
print(dog1.get_age())
print(dog2.bark())
print(dog2.get_age())
print(dog1.species)
print(dog2.species)
#print(dog1.__age)
print(dog1)

print()
print("Cat class")

cat1=Cat("Buddy",3)
cat2=Cat("Charlie",5)
print(cat1.mew())
print(cat1.get_age())
print(cat2.mew())
print(cat2.get_age())
print(cat1.species)
print(cat2.species)
#print(cat1.__age)
print(cat2)
#print(cat1._str_())