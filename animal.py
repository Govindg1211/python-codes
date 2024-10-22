class Animal:
    def __init__(self,name,age):
        self.name=name
        #self.__age=age  (Private property)
        self.age=age
    def get_age(self):
        return f"{self.name} is {self.age} years old."
    def __str__(self): #Return meaningful output when someone prints a object
        return f"{self.name} is {self.age} years old."