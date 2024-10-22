from animal import Animal

class Cat(Animal):
    species="cat species"
    def mew(self):
        return f"{self.name} says meow!"
    
