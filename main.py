from dog import Dog
from cat import Cat

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